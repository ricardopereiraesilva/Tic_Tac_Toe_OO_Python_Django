let empty_p_image = '/static/images/empty.gif';
let red_p_image = '/static/images/red.gif';
let white_p_image = '/static/images/white.gif';

function get_temporaryId() {
	let jv_local_id = localStorage.getItem("jv_local_id");
	let d = new Date();
	let aTime = d.getTime();
	let timeString = aTime.toString(10);
	let truncatedTimeString = timeString.slice(6, 13);
	let newTempIdValue  = parseInt(truncatedTimeString);
	if (jv_local_id == null) {	
		localStorage.setItem("jv_local_id", newTempIdValue);
	}
	return jv_local_id;
}

function positionClick(aLine, aColumn) {
  let id = get_temporaryId();
  let stringId = id+'/'+aLine+'/'+aColumn;
  let url = stringId
  let httpRequester = new XMLHttpRequest(); //******************* AJAX **********************
  httpRequester.open('GET', url)
  httpRequester.onreadystatechange = () => {
        if(httpRequester.readyState == 4 && httpRequester.status == 200) {		//******* TRATAMENTO DO RETORNO DA REQUISIÇÃO
            let backEndArrayFeedback = JSON.parse(httpRequester.responseText)
            document.getElementById("message").innerHTML = backEndArrayFeedback[0];
            updateBoard(backEndArrayFeedback[1][0])
        }
  }
  httpRequester.send() // envio da requisição http
}

function refresh() {
  let id = get_temporaryId();
  let url = `${id}`
  let httpRequester = new XMLHttpRequest(); //******************* AJAX **********************
  httpRequester.open('GET', url)
  httpRequester.onreadystatechange = () => {
        if(httpRequester.readyState == 4 && httpRequester.status == 200) {		//******* TRATAMENTO DO RETORNO DA REQUISIÇÃO
            let backEndArrayFeedback = JSON.parse(httpRequester.responseText)
            document.getElementById("message").innerHTML = backEndArrayFeedback[0];
            updateBoard(backEndArrayFeedback[1][0])
        }
  }
  httpRequester.send() // envio da requisição http
}

function updateBoard(boardArray) {
	let  imageObject = null
	let value = null
	for (let i = 0; i<3; i++) {
		for (let j = 0; j<3; j++) {
			value = boardArray[i][j]
			let im_id = "im"+(i+1)+(j+1)
			imageObject = document.getElementById(im_id)
			if (value==0) {imageObject.src = empty_p_image}
			if (value==1) {imageObject.src = red_p_image}
			if (value==2) {imageObject.src = white_p_image}
		}
	}
}
