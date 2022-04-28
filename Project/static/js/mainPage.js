function showHidePass(element_id) {
	if (document.getElementById(element_id)) {
		let pass = document.getElementById(element_id)
		if (pass.getAttribute('type') === 'password') {
			pass.setAttribute('type', 'text')
		}
		else {
			pass.setAttribute('type', 'password')
		}
	}
}

function showHide(element_id, option) {
	if (document.getElementById(element_id)) {
		let obj = document.getElementById(element_id);
		let back = document.getElementById('background');

		if (option === 'log') {
			back.setAttribute('onclick', 'showHide(\'loginWindow\', \'log\')');
		}
		if (option === 'reg') {
			back.setAttribute('onclick', 'showHide(\'registerWindow\',\'reg\')');
		}

		if (obj.style.display !== "block") {
			obj.style.display = "block";
			back.style.display = 'flex';
		} else {

			if (option === "log") {
				document.getElementById("login").value = '';
				document.getElementById('password').value = '';
				document.getElementById('checkbox').checked = false;
				showHidePass('password');
			}
			if (option === 'reg') {
				document.getElementById("login1").value = '';
				document.getElementById('password1').value = '';
				document.getElementById('password2').value = '';
				document.getElementById('checkbox1').checked = false;
				showHidePass('password1');
			}

			obj.style.display = 'none'
			back.style.display = 'none';
			back.removeAttribute('onclick')
		}
	}
}
