function download_hentai(){
  var data = document.getElementById("kode-nuklir").value
  eel.download_hentai(data)
}

function preview(){
  var data = document.getElementById("kode-nuklir").value
  eel.preview(data)(changepic)
}

function changepic(source){
  document.getElementById("comic-pic").src = source
}
