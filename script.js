let popup = document.getElementsByClassName("num"),
	popupClose = document.getElementsByClassName("closeBtn"),
	popupInfo = document.getElementsByClassName("popupInfo");
popup.onclick = function(){
	popupInfo.style.display = "block";
};
popupClose.onclick = function(){
	popupInfo.style.display = "none";
};
