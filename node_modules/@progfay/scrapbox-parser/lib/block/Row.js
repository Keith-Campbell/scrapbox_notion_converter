"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseToRows = void 0;
const parseToRows = (input) => input.split("\n").map((text) => {
    var _a, _b, _c;
    return ({
        indent: (_c = (_b = (_a = /^\s+/.exec(text)) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b.length) !== null && _c !== void 0 ? _c : 0,
        text,
    });
});
exports.parseToRows = parseToRows;
//# sourceMappingURL=Row.js.map