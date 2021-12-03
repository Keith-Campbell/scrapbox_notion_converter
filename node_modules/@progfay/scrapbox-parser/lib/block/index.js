"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.convertToBlock = void 0;
const Title_1 = require("./Title");
const CodeBlock_1 = require("./CodeBlock");
const Table_1 = require("./Table");
const Line_1 = require("./Line");
const convertToBlock = (pack) => {
    switch (pack.type) {
        case "title":
            return (0, Title_1.convertToTitle)(pack);
        case "codeBlock":
            return (0, CodeBlock_1.convertToCodeBlock)(pack);
        case "table":
            return (0, Table_1.convertToTable)(pack);
        case "line":
            return (0, Line_1.convertToLine)(pack);
    }
};
exports.convertToBlock = convertToBlock;
//# sourceMappingURL=index.js.map