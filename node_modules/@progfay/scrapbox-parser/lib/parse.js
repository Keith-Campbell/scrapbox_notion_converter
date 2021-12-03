"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getTitle = exports.parse = void 0;
const block_1 = require("./block");
const Row_1 = require("./block/Row");
const Pack_1 = require("./block/Pack");
const parse = (input, opts) => {
    var _a;
    const rows = (0, Row_1.parseToRows)(input);
    const packs = (0, Pack_1.packRows)(rows, { hasTitle: (_a = opts === null || opts === void 0 ? void 0 : opts.hasTitle) !== null && _a !== void 0 ? _a : true });
    return packs.map(block_1.convertToBlock);
};
exports.parse = parse;
const getTitle = (input) => {
    var _a, _b;
    const match = /^\s*\S.*$/m.exec(input);
    return (_b = (_a = match === null || match === void 0 ? void 0 : match[0]) === null || _a === void 0 ? void 0 : _a.trim()) !== null && _b !== void 0 ? _b : "Untitled";
};
exports.getTitle = getTitle;
//# sourceMappingURL=parse.js.map