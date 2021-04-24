let popup = document.getElementById("Eugene1"),
	popupClose = document.getElementById("closeBtn"),
	popupInfo = document.getElementById("popupInfo");
popup.onclick = function(){
	popupInfo.style.display = "block";
};
popupClose.onclick = function(){
	popupInfo.style.display = "none";
};
