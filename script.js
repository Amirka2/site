
$('body').on('click', '.passwordCheckbox', function(){
	if ($(this).is(':checked'))
		{
			$('#userPassword').attr('type', 'text');
		} 
	else 
		{
			$('#userPassword').attr('type', 'password');
		}
});

function show_hide_password(target){
	var input = document.getElementById('password-input');
	if (input.getAttribute('type') == 'password') {
		target.classList.add('view');
		input.setAttribute('type', 'text');
	} else {
		target.classList.remove('view');
		input.setAttribute('type', 'password');
	}
	return false;
}

let popup = document.getElementById("Eugene1"),
	popupClose = document.getElementById("closeBtn"),
	popupInfo = document.getElementById("popupInfo");
popup.onclick = function(){
	popupInfo.style.display = "block";
};
popupClose.onclick = function(){
	popupInfo.style.display = "none";
};
