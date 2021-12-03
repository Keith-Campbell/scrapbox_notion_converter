import { parse } from "@progfay/scrapbox-parser";
import fetch from "node-fetch";

const PROJECT_NAME = "atshhandelssohn-54351265";
const PAGE_NAME = "イシュードリブンを無理やり嵌め込もうとするとうまくまとまらない";

fetch(`https://scrapbox.io/api/pages/${PROJECT_NAME}/${PAGE_NAME}/text`)
  .then((response) => response.text())
  .then((text) => parse(text));