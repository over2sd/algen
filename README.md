algen
=====

Algebra problem generator for teachers and tutors

This program generates random numbers in a given range and uses them to
generate algebra exercises of the desired type(s).

Option flags:

-c <#>, --count <#>:		How many exercises to generate

-n <#>, --min <#>:		Minimum value for variable, coefficients,

	and constants

-x <#>, --max <#>:		Maximum value for variable, coefficients,

	and constants

-v <char|string>, --vars <char|string>:		String of lowercase letters

	that can be used for variables

	Examples: "-v x", "-v abc"

-o <file>, --outfile <file>:		A filename where the program will

	append its results for easy copy/paste

-t <types>, --types <types>:		Type(s) of exercises to generate:

	Examples: "-t 138af" "-t 2"

-0, --allowzero:		Allow value of x, a, b, c... to be

	boring (0, 1, or -1)

-u <string>, --unit <string>:		Text to put after measurements

	(e.g., knots)

-a, --wholealt:		Do not allow decimal points in altitudes
