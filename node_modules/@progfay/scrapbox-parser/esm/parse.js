import { convertToBlock } from "./block";
import { parseToRows } from "./block/Row";
import { packRows } from "./block/Pack";
export const parse = (input, opts) => {
    var _a;
    const rows = parseToRows(input);
    const packs = packRows(rows, { hasTitle: (_a = opts === null || opts === void 0 ? void 0 : opts.hasTitle) !== null && _a !== void 0 ? _a : true });
    return packs.map(convertToBlock);
};
export const getTitle = (input) => {
    var _a, _b;
    const match = /^\s*\S.*$/m.exec(input);
    return (_b = (_a = match === null || match === void 0 ? void 0 : match[0]) === null || _a === void 0 ? void 0 : _a.trim()) !== null && _b !== void 0 ? _b : "Untitled";
};
//# sourceMappingURL=parse.js.map