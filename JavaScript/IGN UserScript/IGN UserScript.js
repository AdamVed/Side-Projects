// ==UserScript==
// @name         IGN UX Enhancement
// @namespace    http://violentmonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.ign.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ign.com
// @grant        GM_xmlhttpRequest
// @run-at       document-end
// ==/UserScript==


(function () {
  "use strict";
  const badGames = [
    "Destiny 2",
    "Genshin Impact",
    "MLB",
    "NBA",
    "Diablo 4",
    "Diablo IV",
    "Sims 4",
    "FIFA",
  ];
  const badDeals = [
    "$",
    "%",
    "IGN Store",
    "Deal Alert",
    "Daily Deals",
    "Deal",
    "Deals",
    "Coupons",
    "Sale",
    "Giveaway",
    "Discount",
    "Black Friday",
    "Price",
    "Cheap",
    "Free",
    "Amazon Prime Day",
  ];
  const badSpam = [
    "Podcast",
    "IGN The Fix",
    "IGN The Weekly Fix",
    "IGN Daily Fix",
  ];
  const badOther = [
    "PlayStation Plus",
    "Amiibo",
    "PS Plus",
    "Monitor",
    "monitor",
    "headphones",
    "Headphones",
  ];
  const blacklist = badGames.concat(badDeals).concat(badSpam).concat(badOther);

  // for prevention of repeating errors in the console during debugging
  const ignores = [];

  const blockCardDivs = function() {
    // Select all divs with 'card' in the class attribute
    const cardDivs = document.querySelectorAll('div[class*="card"]');

    for (let div of cardDivs) {
      // Remove each div from the document
      div.remove();
    }
  };

  // block of articles is found under "main-content". It only shows the currently loaded MainContents which is part of the reason we need to do it again every few seconds
  const getMainContents = function () {
    const mainContents = document.querySelectorAll('[class="main-content"]');
    if (!mainContents) {
      console.log("mainContent missing!\n");
    }
    return mainContents;
  };

  // "items" are individual articles within a main-content (one main-content has about 7 items=articles)
  const getItemsFromMainContent = function (mainContent) {
    const items = mainContent.querySelectorAll('[class="item-body"]');
    if (!items) {
      console.log("items missing!\n");
    }
    return items;
  };

  // a stack here is the trio of related content, author name and number of comments. We use the stack to append the new paragraph as author's child
  const getStackFromItem = function (item) {
    const stack = item.querySelector(
      '[class="stack jsx-2043432607 item-more-data"]'
    );
    return stack;
  };

  const getItemTitle = function (item) {
    return item.ariaLabel;
  };

  const isTitleBlacklisted = function (item) {
    const title = getItemTitle(item);
    if (!title) {
      return false;
    }
    for (const name of blacklist) {
      if (title.includes(name)) {
        return true;
      }
    }
    return false;
  };

  const removeEmptyRows = function () {
    const dividers = document.getElementsByClassName(
      "content-item jsx-1409608325 row divider"
    );

    for (let divider of dividers) {
      if (divider.children.length === 0) {
        divider.remove();
      }
    }
  };

  //simply extracts the string url of the article=item we're dealing with
  const getLinkFromItem = function (item) {
    const link = item.href;
    if (!link) {
      console.log("link missing!\n item = ", item);
    }
    return link;
  };

  // in order to only send the http requests to articles that have "review" in their url
  const isLinkReview = function (url) {
    return url.includes("review");
  };

  // sends http request of the article we're dealing with in order for us to extract the review score
  const getPage = function (url, callback) {
    GM_xmlhttpRequest({
      method: "GET",
      url: url,
      onload: callback,
    });
  };

  // extract the rating value from getPage html response
  const getReviewScore = function (pageSource) {
    const anchor = '"score":';
    const leftIndex = pageSource.indexOf(anchor);
    const chunk = pageSource.substring(
      leftIndex + anchor.length,
      leftIndex + anchor.length + 2
    );
    const score = isNaN(chunk[chunk.length - 1]) ? chunk[0] : chunk;
    const scoreNumber = parseInt(score);

    return !isNaN(scoreNumber) ? scoreNumber : null;
  };

  const getScoreSummary = function (pageSource) {
    const anchor = '"scoreSummary":"';
    const rightAnchor = '","verdict';
    const leftIndex = pageSource.indexOf(anchor);
    const rightIndex = pageSource.indexOf(rightAnchor);
    let summary = pageSource.substring(leftIndex, rightIndex);
    summary = summary.replace(anchor, "");
    return summary;
  };

  const getAuthor = function (stack) {
    const author = stack.querySelector(
      '[class="caption jsx-1541923331 data small"]'

    );

    if (!author) {
      console.log("author missing!\n stack = ", stack);
    }
    return author;
  };

  const appendScore = function (score, summary, author) {
    if (score && summary && author.children.length === 1) {
      const pScore = document.createElement("p");
      pScore.innerHTML = (window.location.href.includes("reviews") ? "Summary" : "<br>\t\tIGN Score: " + score);
      console.log("window.location.href = ", window.location.href);
      console.log("window.location.href.includes(reviews)", window.location.href.includes("reviews"));
      pScore.style.color = "red";
      pScore.style.fontSize = "11px";
      author.setAttribute("title", summary);
      author.appendChild(pScore);
    }
  };

  // main function
  const run = function () {
    const mainContents = getMainContents();

    // Block divs that have "card" in its name which should cover all the spammy card stuff
    blockCardDivs();

    for (let mainContent of mainContents) {
      const items = getItemsFromMainContent(mainContent);
      if (!items) {
        continue;
      }

      for (let item of items) {
        if (isTitleBlacklisted(item)) {
          item.remove();
          removeEmptyRows();
          continue;
        }

        const link = getLinkFromItem(item);
        if (!isLinkReview(link)) {
          continue;
        }

        const stack = getStackFromItem(item);
        if (!stack) {
          const ERR = "stack missing for link: " + link;
          if (!ignores.includes(ERR)) {
            console.log(ERR);
            ignores.push(ERR);
          }
          continue;
        }

        getPage(link, function (response) {
          const score = getReviewScore(response.responseText);
          const summary = getScoreSummary(response.responseText);
          const author = getAuthor(stack);
          appendScore(score, summary, author);
        });
      }
    }
  };
  window.setInterval(run, 2000);
})();
