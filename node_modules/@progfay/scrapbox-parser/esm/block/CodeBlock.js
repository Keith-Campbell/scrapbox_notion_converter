export const convertToCodeBlock = (pack) => {
    const { rows: [head, ...body], } = pack;
    const { indent = 0, text = "" } = head !== null && head !== void 0 ? head : {};
    const fileName = text.replace(/^\s*code:/, "");
    return {
        indent,
        type: "codeBlock",
        fileName,
        content: body
            .map((row) => row.text.substring(indent + 1))
            .join("\n"),
    };
};
//# sourceMappingURL=CodeBlock.js.map