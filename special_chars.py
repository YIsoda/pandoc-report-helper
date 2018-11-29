from panflute import run_filter, Str


class Special:
	non_breaking_space = '\xA0'
	mu = 'μ'


def unit_ul(elem, doc):
	if type(elem) == Str:
		elem.text = elem.text \
			.replace('uL', Special.non_breaking_space + Special.mu + 'L') \
			.replace('mmol', Special.non_breaking_space + 'mmol')
		return elem


def main(doc=None):
	return run_filter(unit_ul, doc=doc)


if __name__ == '__main__':
	main()
