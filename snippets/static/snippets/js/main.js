document.addEventListener("DOMContentLoaded", function () {

    const copyButton = document.querySelector(".copy-btn");

    if (copyButton) {

        copyButton.addEventListener("click", async function () {

            const code = document.querySelector(".code-block code");

            if (!code) return;

            try {
                await navigator.clipboard.writeText(code.textContent);

                copyButton.textContent = "Copied!";

                setTimeout(function () {
                    copyButton.textContent = "Copy Code";
                }, 1500);

            } catch (error) {
                copyButton.textContent = "Copy failed";
            }

        });

    }

});