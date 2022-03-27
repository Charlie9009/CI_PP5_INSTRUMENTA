// Sorting button
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
        window.location.replace(currentUrl);
    }
})

// Listen for change in imagefield
$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

// Back to top button
$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})