import type { ParserOption } from "../parse";
import type { CodeBlockPack } from "./CodeBlock";
import type { LinePack } from "./Line";
import type { Row } from "./Row";
import type { TablePack } from "./Table";
import type { TitlePack } from "./Title";
export declare type Pack = TitlePack | CodeBlockPack | TablePack | LinePack;
export declare const packRows: (rows: Row[], opts: ParserOption) => Pack[];
//# sourceMappingURL=Pack.d.ts.map