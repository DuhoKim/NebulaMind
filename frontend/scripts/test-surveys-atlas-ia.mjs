import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { createRequire } from 'node:module';
import vm from 'node:vm';
import ts from 'typescript';

const require = createRequire(import.meta.url);

const root = process.cwd();
const path = (...parts) => join(root, ...parts);
const read = (...parts) => readFileSync(path(...parts), 'utf8');

const surveysPage = read('src/app/surveys/page.tsx');
const controlBar = read('src/components/surveys/ControlBar.tsx');
const surveysView = read('src/components/surveys/SurveysView.tsx');
const chartView = read('src/components/surveys/ChartView.tsx');
const plotA = read('src/components/surveys/PlotA.tsx');
const surveyCard = read('src/components/surveys/SurveyCard.tsx');
const bandSpectrumStrip = read('src/components/surveys/BandSpectrumStrip.tsx');
const constants = read('src/components/surveys/constants.ts');
const plottingPath = path('src/components/surveys/plotting.ts');
const plotting = existsSync(plottingPath) ? readFileSync(plottingPath, 'utf8') : '';

const compiledConstants = ts.transpileModule(constants, {
  compilerOptions: {
    module: ts.ModuleKind.CommonJS,
    target: ts.ScriptTarget.ES2019,
    strict: true,
  },
  fileName: path('src/components/surveys/constants.ts'),
});
const constantsModule = { exports: {} };
vm.runInNewContext(
  compiledConstants.outputText,
  { module: constantsModule, exports: constantsModule.exports, require },
  { filename: path('src/components/surveys/constants.ts') },
);
const {
  parseBandParam,
  parsePlotTypeParam,
  parseStatusesParam,
} = constantsModule.exports;

assert.match(
  surveysPage,
  /Astronomical Surveys & Facilities/,
  'Surveys page should use honest Surveys & Facilities scope copy.',
);
assert.match(
  surveysPage,
  /observational programs, facilities, and survey data products/,
  'Surveys subtitle should describe mixed survey/facility/data-product scope.',
);
assert.match(
  surveysPage,
  /survey-page__stats/,
  'Surveys page should expose a lightweight stats row once data is loaded.',
);

assert.match(controlBar, />\s*List\s*</, 'Mode toggle should show List, not Directory.');
assert.match(controlBar, />\s*Explorer\s*</, 'Mode toggle should show Explorer, not Chart.');
assert.doesNotMatch(controlBar, />\s*Directory\s*</, 'Directory label should be removed from visible toggle copy.');
assert.doesNotMatch(controlBar, />\s*Chart\s*</, 'Chart label should be removed from visible toggle copy.');
assert.match(controlBar, /role="group"/, 'Mode toggle should expose grouped segmented-control semantics.');
assert.match(controlBar, /aria-label="Survey view mode"/, 'Mode toggle should expose an accessible group name.');
assert.match(controlBar, /aria-pressed=\{view === "directory"\}/, 'List toggle should expose pressed state.');
assert.match(controlBar, /aria-pressed=\{view === "chart"\}/, 'Explorer toggle should expose pressed state.');
assert.match(controlBar, /aria-label="Search surveys by name, operator, or science goals"/, 'Search input should expose a descriptive accessible name.');
assert.match(controlBar, /aria-label="Open survey filters"/, 'Filter trigger should expose a descriptive accessible name.');

assert.doesNotMatch(
  surveysView,
  /state\.checkedStatuses\.sort\(/,
  'URL sync should not mutate reducer state with state.checkedStatuses.sort().',
);
assert.match(
  surveysView,
  /\[\.\.\.state\.checkedStatuses\]\.sort\(/,
  'URL sync should copy checkedStatuses before sorting.',
);

assert.match(chartView, /plotted/i, 'Chart header should distinguish plotted rows from matching filters.');
assert.match(chartView, /matching filters/i, 'Chart header should mention matching filters.');
assert.match(chartView, /Map surveys by physical reach/i, 'Chart should explain Atlas/Explorer purpose.');
assert.match(chartView, /missing-data rows/i, 'Chart should explain that missing-data rows are not silently dropped.');

assert.match(plotA, /role="img"/, 'Plot SVG should expose image semantics.');
assert.match(plotA, /aria-labelledby/, 'Plot SVG should link to an accessible title/description.');
assert.match(plotA, /aria-expanded=\{missingExpanded\}/, 'Not-plotted disclosure button should expose aria-expanded state.');
assert.match(plotA, /aria-controls=\{missingListId\}/, 'Not-plotted disclosure button should point at its controlled list region.');
assert.match(plotA, /id=\{missingListId\}/, 'Not-plotted detail region should expose the ID referenced by aria-controls.');
assert.match(plotA, /pts\.length <= 15/, 'Plot should keep persistent labels only for low-density views.');
assert.match(plotA, /not plotted/, 'Plot should keep the missing-data chip language.');
assert.match(
  plotA,
  /const renderMissingSurveys = \(\) => \(/,
  'PlotA should centralize the not-plotted chip/list so it can render in both plotted and zero-plotted states.',
);
assert.match(
  plotA,
  /surveys\.length > 0[\s\S]*renderMissingSurveys\(\)/,
  'When filters match surveys but zero points are plottable, PlotA should still render the not-plotted chip/list.',
);

assert.ok(existsSync(plottingPath), 'Plotting helpers should live in a shared plotting.ts module.');
assert.match(plotting, /export const AXIS_OPTIONS/, 'Axis options should be exported from shared plotting helpers.');
assert.match(plotting, /export function getSurveyAxisValue/, 'Shared plotting helpers should expose the axis-value conversion function.');
assert.match(plotting, /export function surveyHasPlottableAxes/, 'Shared plotting helpers should expose the plottability predicate.');
assert.match(plotting, /export function parseAxisParam/, 'Shared plotting helpers should validate URL axis params with a fallback.');
assert.match(surveysView, /parseAxisParam\(params\.get\("xaxis"\), "wavelength_center_um"\)/, 'Initial xAxis should validate malformed URL params before storing reducer state.');
assert.match(surveysView, /parseAxisParam\(params\.get\("yaxis"\), "z_max"\)/, 'Initial yAxis should validate malformed URL params before storing reducer state.');
assert.match(constants, /export function parseBandParam/, 'Band URL params should be validated by a shared helper.');
assert.match(constants, /export function parseStatusesParam/, 'Status URL params should be validated by a shared helper.');
assert.match(constants, /export function parsePlotTypeParam/, 'Plot type URL params should be validated by a shared helper.');
assert.match(surveysView, /parseBandParam\(params\.get\("band"\), "all"\)/, 'Initial band should validate malformed URL params before storing reducer state.');
assert.match(surveysView, /parseStatusesParam\(statusesParam\)/, 'Initial status filters should drop malformed URL params before storing reducer state.');
assert.match(surveysView, /parsePlotTypeParam\(params\.get\("plottype"\), "wavelength_redshift"\)/, 'Initial plot type should validate malformed URL params before storing reducer state.');
assert.equal(parseBandParam('optical', 'all'), 'optical', 'Valid band URL params should be preserved.');
assert.equal(parseBandParam('not-a-band', 'all'), 'all', 'Malformed band URL params should fall back to all bands.');
assert.deepEqual(
  Array.from(parseStatusesParam('operational,not-a-status,retired,operational')),
  ['operational', 'retired'],
  'Status URL params should de-dupe and drop unknown status IDs.',
);
assert.deepEqual(
  Array.from(parseStatusesParam('not-a-status')),
  ['operational', 'commissioning', 'planned', 'retired'],
  'Fully malformed status URL params should fall back to default statuses.',
);
assert.equal(parsePlotTypeParam('depth_sources', 'wavelength_redshift'), 'depth_sources', 'Valid plot type URL params should be preserved.');
assert.equal(parsePlotTypeParam('not-a-plot', 'wavelength_redshift'), 'wavelength_redshift', 'Malformed plot type URL params should fall back safely.');
assert.match(surveysView, /p\.set\("statuses", sortedCheckedStatuses\.join\(","\)\)/, 'Status URL sync should write a stable canonical status order.');
assert.match(chartView, /from "\.\/plotting"/, 'ChartView should import shared plotting helpers.');
assert.match(plotA, /from "\.\/plotting"/, 'PlotA should import shared plotting helpers.');
assert.doesNotMatch(chartView, /function isPlottable/, 'ChartView should not keep a private plottability predicate.');
assert.doesNotMatch(chartView, /statusOpSurveys/, 'ChartView should not expose the unused statusOpSurveys prop.');
assert.doesNotMatch(surveysView, /statusOpSurveys=\{statusOpSurveys\}/, 'SurveysView should not pass the unused ChartView statusOpSurveys prop.');

assert.match(surveyCard, /<button\s+className="survey-card"/, 'Survey cards should be real buttons, not generic clickable divs.');
assert.match(surveyCard, /type="button"/, 'Survey card button should declare type="button".');
assert.match(surveyCard, /aria-label=\{`Open \$\{survey\.name\} survey details`\}/, 'Survey card should expose a descriptive accessible name.');
assert.doesNotMatch(surveyCard, /<div\s+className="survey-card"/, 'Survey cards should not use a root clickable div.');
assert.match(bandSpectrumStrip, /<button\s+className=\{`band-seg/, 'Band strip segments should be real buttons.');
assert.match(bandSpectrumStrip, /aria-pressed=\{band === "all"\}/, 'All-band segment should expose selected state.');
assert.match(bandSpectrumStrip, /aria-pressed=\{active\}/, 'Band segments should expose selected state.');
assert.match(bandSpectrumStrip, /disabled=\{count === 0\}/, 'Empty band segments should be disabled rather than pointer-event-only divs.');
assert.match(bandSpectrumStrip, /aria-label=\{`Filter to \$\{BAND_LABELS_LONG\[bId\]\}/, 'Band segments should expose filter intent and band label.');

console.log('surveys atlas IA smoke checks passed');
