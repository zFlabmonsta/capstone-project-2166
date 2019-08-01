var itemsCount = 0,
    itemsMax = $('.outer div').length;
$('.outer div').hide();
console.log(itemsMax);
const p = document.querySelector('#page');
pag = p.dataset.n;

function showNextItems() {
    var pagination = pag;
    
    for (var i = itemsCount; i < (itemsCount + pagination); i++) {
        $('.outer div:eq(' + i + ')').show();
    }

    itemsCount += pagination;
    
    if (itemsCount > itemsMax) {
        $('#showMore').hide();
    }
};

showNextItems();

$('#showMore').on('click', function (e) {
    e.preventDefault();
    showNextItems();
});
