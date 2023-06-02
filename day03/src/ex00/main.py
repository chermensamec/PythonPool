from bs4 import BeautifulSoup


def main():
    with open('../../materials/evilcorp.html', 'r') as page:
        parser = BeautifulSoup(page, 'html.parser')   
    parser.head.title.string = 'Evil Corp - Stealing your money every day'
    print(parser.head.title.string)
    print(parser.find('name'))
    print(parser.body.p.span.string)

main()
