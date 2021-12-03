"use strict";
exports.__esModule = true;
var scrapbox_parser_1 = require("@progfay/scrapbox-parser");
var node_fetch_1 = require("node-fetch");
var PROJECT_NAME = "atshhandelssohn-54351265";
var PAGE_NAME = "イシュードリブンを無理やり嵌め込もうとするとうまくまとまらない";
node_fetch_1["default"]("https://scrapbox.io/api/pages/" + PROJECT_NAME + "/" + PAGE_NAME + "/text")
    .then(function (response) { return response.text(); })
    .then(function (text) { return scrapbox_parser_1.parse(text); });
