function putDescriptionText(text) {
    console.log(text)
    document.getElementById('edit-description').innerHTML = text;
}

function checkedBox(id, is_checked) {
    if (is_checked == "True") {
        document.getElementById(id).checked = true;
    }
}


