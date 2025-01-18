rule GenericVTwoRule
{
	meta:
		description = "Generic password parser version two"
		author = "FH"
		date = "2025-01-17"
		version = "1.0"
		mwcp = "CredentialFinder.GenericVTwo"

	strings:
		$regex = /username:[^\n]*\npassword:[^\n]*\nwebsite:[^\n]*[\n$]/
	condition:
		any of them
}

rule GenericVOneRule
{
	meta:
		description = "Generic password parser version one"
		author = "FH"
		date = "2025-01-17"
		version = "1.0"
		mwcp = "CredentialFinder.GenericVOne"

	strings:
		$regex = /[uU][Rr][Ll]\s*[^\s]\s*[^\n]*\n\s*[Uu]sername\s*[^\s]\s*[^\n]*\n\s*[Pp]assword\s*[^\s]\s*[^\n]*[\n$\s]/
	condition:
		any of them
}

rule AzVOne
{
	meta:
		description = "Az version one"
		author = "FH"
		date = "2025-01-17"
		version = "1.0"
		mwcp = "CredentialFinder.AzVOne"
	strings:
		$regex = /SOFT:[^\n]*\nURL:[^\n]*\nUSER:[^\n]*\nPASS:[^\n]*[\n$]/
	condition:
		any of them
}

rule AzVTwo
{
	meta:
		description = "Az version two"
		author = "FH"
		date = "2025-01-18"
		version = "1.0"
		mwcp = "CredentialFinder.AzVTwo"
	strings:
		$regex = /Browser:\s*[^\n]*\nUrl:\s*[^\n]*\nLogin:\s*[^\n]*\nPass:\s*[^\n]*[\n$]/
	condition:
		any of them
}