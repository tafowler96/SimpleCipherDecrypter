var API_ENDPOINT = "https://md08fdwxhi.execute-api.us-east-1.amazonaws.com/dev/simpleCipherDecrypt"

document.getElementById("decryptButton").onclick = function(){
	var inputData = {
		"cipherText": $('#cipherText').val()
	};

	$.ajax({
	    url: API_ENDPOINT,
	    type: 'POST',
	    data:  JSON.stringify(inputData),
		contentType: 'application/json; charset=utf-8',
	    success: function (response) {
			document.getElementById("plainText").textContent=response["body"]["plainText"];
			document.getElementById("key").value=response["body"]["key"];
	    },
	    error: function (xhr, exception) {
			console.log(xhr);
			console.log("error");
		}
	});
}