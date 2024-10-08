function CheckConsoleHost {
	$users = Get-ChildItem -Path C:\Users\ -Exclude "Public","Default","All Users","Default User" | Select-Object -ExpandProperty FullName
	foreach ($user in $users) {
		Write-Host "Found:",$user
		$userPath = "$user\AppData\Roaming\Microsoft\Windows\"
		try {
			$tmp = Get-ChildItem -Path $userPath -Force -Recurse -Depth 3 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
			foreach ($path in $tmp) {
				if ($path -like "*PSReadLine\ConsoleHost_history.txt") {
					Write-Host "History:" -ForegroundColor Blue -NoNewline
					Write-Host $path -ForegroundColor Green
					Get-Content $path
				}
			}
		} catch {
			Write-Warning "Access denied.`n"
		}
	}
}

function CheckFiles {	
	$users = Get-ChildItem -Path C:\Users\ -Exclude "Public","Default","All Users","Default User" | Select-Object -ExpandProperty FullName
	foreach ($user in $users) {
		Write-Host "Found:",$user
		$userPath = "$user"
		try {
			$tmp = Get-ChildItem -Force -Path $userPath -Recurse -Include *.txt,*.cfg,*.kdbx,*.config,*.cnf,*.back,*.bck,*.doc,*.docx,*.zip,*.pdf,*.xls,*.xlsx  -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
			foreach ($file in $tmp) {
				Write-Host $file
			}
		} catch {
			Write-Warning "Access denied.`n"
		}
	}
}
