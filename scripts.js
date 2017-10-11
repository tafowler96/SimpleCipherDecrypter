var API_ENDPOINT = "YOUR-API-GATEWAY-HERE"

document.getElementById("decryptButton").onclick = function(){

	var inputData = {
		"cipherText": $('#cipherText').val(),
		"key" : $('#key').val()
	};

	$.ajax({
	      url: API_ENDPOINT,
	      type: 'POST',
	      data:  JSON.stringify(inputData),
	      contentType: 'application/json; charset=utf-8',
	      success: function (response) {
					document.getElementById("postIDreturned").textContent=response;
	      },
	      error: function () {
	          alert("error");
	      }
	  });
}