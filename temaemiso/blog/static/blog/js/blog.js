document.addEventListener("DOMContentLoaded", function () {
    setCodeCopyBehavior();
});

/**
 * コピーボタンの挙動
 */
function setCodeCopyBehavior() {
    // preList = document.querySelectorAll(":not(.is-loaded).language-shell");
    preList = document.querySelectorAll("pre");
    preList.forEach(function (element) {
        // コピーボタンの要素を取得
        copyButton = element.querySelector(".copy-code-button");
        copyButton.onclick = function () {
            // codeタグのinnerTextを取得
            console.log("element", element);
            code = element.querySelector("span").innerText;
            // クリップボードへ保管
            navigator.clipboard.writeText(code);
            // toastrを設定
            toastr.options = {
                // 1.5秒で消える設定
                timeOut: "1500",
            }
            // toastrを起動
            toastr["info"]("コピーされました！");
        }
    });
}