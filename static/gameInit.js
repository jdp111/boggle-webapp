

counter = 1;
score = 0;
words = [];

function showWord(word){
  $bankfill = $(`<div class = 'word'>${word}</div>`)
  $(`#col${counter}`).append($bankfill)

  if (counter < 3 ){
    counter +=1;
  }
  else{counter = 1}
}

function showScore(){
  console.log(score)
  $(".score").text(score)
}

function showMessage(message){
  alert(message);
}


async function testWord(word){

  const resp = await axios.get("/check-word", { params: { word: word }});
  console.log(resp.data.result)
  if (resp.data.result == 'not-word') {
    showMessage(`${word} is not a valid English word`, "err");
  } else if (resp.data.result == 'not-on-board') {
    showMessage(`${word} is not a valid word on this board`, "err");
  } else if (words.includes(word)){
    showMessage("repeat word")
  } else {
    words.push(word);
    showWord(word);
    console.log(word)
    score += word.length;
    console.log(score);
    showScore();
  
  }
}

$('#subbut').click(function(){
  testWord($('#form').val())
  console.log($('#form').val())
  $('#form').val("");
})
