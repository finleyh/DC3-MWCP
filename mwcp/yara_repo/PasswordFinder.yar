rule PasswordRule
{
	meta:
		description = ""
		author = "FH"
		data = "2025-01-17"
		version = "1.0"
		mwcp = "PasswordFinder"

	strings:
		$password = "password" nocase
		$username = "username" nocase
		$url = "url" nocase
		$website = "website"

	condition:
		$password and $username and ($url or $website)	
}
