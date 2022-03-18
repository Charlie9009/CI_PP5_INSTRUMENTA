var toastElList = [].slice.call(document.querySelectorAll('.toast'));
var toastList = toastElList.map(function (toastEl) {
var option = {
    autohide: false,
};
var newToast = new bootstrap.Toast(toastEl, option);
newToast.show();
});