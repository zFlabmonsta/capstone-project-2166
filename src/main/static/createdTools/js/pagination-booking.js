var itemsCountBooking = 0,
    itemsMaxBooking = $('.outerBooking div').length;
$('.outerBooking div').hide();
const pg = document.querySelector('#pageBooking');
pag = pg.dataset.n;

console.log(itemsMaxBooking);

function showNextItemsBooking() {
    var pagination = pag;
    
    for (var i = itemsCountBooking; i < (itemsCountBooking + pagination); i++) {
        $('.outerBooking div:eq(' + i + ')').show();
    }

    itemsCountBooking += pagination;
    
    if (itemsCountBooking > itemsMaxBooking) {
        $('#showMoreBooking').hide();
    }
};

showNextItemsBooking();

$('#showMoreBooking').on('click', function (e) {
    e.preventDefault();
    showNextItemsBooking();
});

