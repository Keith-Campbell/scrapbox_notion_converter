const isChildRowOfPack = (pack, row) => {
    var _a, _b;
    return (pack.type === "codeBlock" || pack.type === "table") &&
        row.indent > ((_b = (_a = pack.rows[0]) === null || _a === void 0 ? void 0 : _a.indent) !== null && _b !== void 0 ? _b : 0);
};
const packing = (packs, row) => {
    const lastPack = packs[packs.length - 1];
    if (lastPack !== undefined && isChildRowOfPack(lastPack, row)) {
        lastPack.rows.push(row);
        return packs;
    }
    packs.push({
        type: /^\s*code:/.test(row.text)
            ? "codeBlock"
            : /^\s*table:/.test(row.text)
                ? "table"
                : "line",
        rows: [row],
    });
    return packs;
};
export const packRows = (rows, opts) => {
    var _a;
    if ((_a = opts.hasTitle) !== null && _a !== void 0 ? _a : true) {
        const [title, ...body] = rows;
        if (title === undefined)
            return [];
        return [
            {
                type: "title",
                rows: [title],
            },
            ...body.reduce(packing, []),
        ];
    }
    return rows.reduce(packing, []);
};
//# sourceMappingURL=Pack.js.map