import click
import requests
from parsel import Selector

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
URL = "http://klukka.dkvistun.is/menningarfelagakureyrar?Length=12"


@click.command()
@click.argument("employee_number")
@click.option("-j", "--jobtype", default=0, show_default=True)
@click.option("-d", "--description", default="")
def main(employee_number, jobtype, description):
    content = requests.get(URL, headers=HEADERS).text

    form_data = {
        "__LASTFOCUS": "",
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "ctl00$_LoginForm$ssn": "",
        "ctl00$_LoginForm$jobtype": "",
        "ctl00$_LoginForm$desc": "",
        "ctl00$_LoginForm$hfGeo": "",
    }

    selector = Selector(content)
    form_data["__VIEWSTATE"] = selector.css("#__VIEWSTATE").attrib["value"]
    form_data["__VIEWSTATEGENERATOR"] = selector.css("#__VIEWSTATEGENERATOR").attrib[
        "value"
    ]
    form_data["ctl00$_LoginForm$ssn"] = f"{employee_number}"
    form_data["ctl00$_LoginForm$jobtype"] = f"{jobtype}"
    form_data["ctl00$_LoginForm$desc"] = f"{description}"

    post_response = requests.post(URL, data=form_data, headers=HEADERS).text
    selector = Selector(post_response)
    if (error := selector.css("#ctl00__LoginForm_lblError::text").get()) is not None:
        click.echo(error, err=True)
    else:
        click.echo(selector.css("#ctl00__LoginForm_lblSuccess::text").get())


if __name__ == "__main__":
    main()
