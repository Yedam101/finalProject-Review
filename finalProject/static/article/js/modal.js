const openModalButtons = document.querySelectorAll("[data-modal-target]");
const closeModalButtons = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");
const modalScore = document.querySelectorAll("[data-result]");
const cateogryNews = document.querySelectorAll(".category-news-lists > li > a");
const inputValue = document.querySelector(".link-input");
const linkSubmit = document.querySelector(".search-box > button");

function evalResult(score) {
  if (score > 49) {
    return { say: "신뢰도 높음", color: "#6de195, #c4e759", class: "high" };
  } else if (50 > score && score > 29) {
    return {
      say: "신뢰도 보통",
      color: "#f8d800,#fdeb71",
      class: "medium",
    };
  } else if (30 > score && score > 19) {
    return {
      say: "신뢰도 낮음",
      color: "#f55555,#fccf31",
      class: "low",
    };
  }
}

function paintModal(news) {
  const newsScore = news.querySelector(".progressbar");
  const temp = evalResult(newsScore.getAttribute("aria-valuenow"));
  newsScore.classList.add(temp.class);
  news.querySelector(".modal-text > h2").innerText = temp.say;
  news.querySelector(".modal-text > h2").style.color = temp.color.substr(0, 7);
  newsScore.style.color = temp.color.substr(0, 7);
}

openModalButtons.forEach((li) => {
  li.addEventListener("click", () => {
    const news = document.querySelector(li.dataset.modalTarget);
    paintModal(news);
    openModal(news);
  });
});

closeModalButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const modal = button.closest(".modal");
    closeModal(modal);
  });
});

function openModal(news) {
  if (news == null) return;
  document.querySelector(".score > button").click();
  news.classList.add("active");
  overlay.classList.add("active");
}

function closeModal(modal) {
  if (modal == null) return;
  modal.classList.remove("active");
  overlay.classList.remove("active");
}

cateogryNews.forEach((a) => {
  a.addEventListener("click", (event) => {
    event.preventDefault();
    const modal = a.closest(".modal");
    closeModal(modal);
    inputValue.value = a.getAttribute("href");
    linkSubmit.click();
    window.scrollTo({ top: 100, behavior: "smooth" });
  });
});
