const result = document.querySelector(".result");
const submitLink = document.querySelector(".search-box");
const inputLink = document.querySelector("input[name='article-link']");
const submitBtn = document.querySelector(".submit");
const resultClose = document.querySelector(".result button");
const score = document.querySelector(".score");

function showResult(news) {
  score.style.display = "flex";
  const scorePress = document.querySelector(".score-detail__press");
  const scoreReporter = document.querySelector(".score-detail__reporter");
  const scoreTime = document.querySelector(".score-detail__time");
  const scoreTitle = document.querySelector(".score-detail__title");
  const scoreImg = document.querySelector(".score-detail__right img");
  const scoreNum = document.querySelector(".score-result__num");
  const scoreText = document.querySelector(".score-result__text");
  const resultImg = document.querySelector(".score-result img");
  scorePress.innerText = news.press;
  if (news.reporter !== "입력 ") {
    scoreReporter.innerText = news.reporter;
  }
  scoreTime.innerText = news.time;
  scoreTitle.innerText = news.title;
  if (news.img !== "video_news") {
    scoreImg.setAttribute("src", news.img);
  } else {
    scoreImg.closest(".score-detail__right").innerText = "사진이 없습니다.";
  }
  resultImg.setAttribute("src", `/static/media/article/wcimg${news.id}.png`);
  tempScore = evalResult(news.result);
  scoreNum.setAttribute("aria-valuenow", parseInt(news.result));
  scoreNum.setAttribute(
    "style",
    `--value: ${parseInt(news.result)}; color:${tempScore.color.substr(0, 7)};`
  );
  scoreNum.classList.remove("high");
  scoreNum.classList.remove("medium");
  scoreNum.classList.remove("low");
  scoreNum.classList.add(tempScore.class);
  scoreText.innerText = tempScore.say;
  scoreText.style.color = tempScore.color.substr(0, 7);
}

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

function onSubmitLink(event) {
  score.style.display = "none";
  result.classList.add("appear");
  event.preventDefault();
  $.ajax({
    url: "result",
    type: "GET",
    data: { inputLink: inputLink.value },
    datatype: "json",
    success: function (data) {
      return showResult(data);
    },
    error: function () {
      result.classList.remove("appear");
      alert("네이버 혹은 다음 을 통한 뉴스 링크를 넣어 주세요!");
    },
  });
}
function handleResultClose(event) {
  event.preventDefault();
  score.style.display = "none";
  result.classList.remove("appear");
}

submitLink.addEventListener("submit", onSubmitLink);
resultClose.addEventListener("click", handleResultClose);
