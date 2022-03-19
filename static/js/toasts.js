/**
 * Javascript for the toast messages. Taken from bootstrap page;
 * https://getbootstrap.com/docs/5.1/components/toasts/#basic
 */

var toastElList = [].slice.call(document.querySelectorAll('.toast'));
var toastList = toastElList.map(function (toastEl) {
var option = {
    autohide: false,
};
var newToast = new bootstrap.Toast(toastEl, option);
newToast.show();
});