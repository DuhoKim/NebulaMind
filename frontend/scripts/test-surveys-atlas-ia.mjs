import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const path = (...parts) => join(root, ...parts);
const read = (...parts) => readFileSync(path(...parts), 'utf8');

const surveysPage = read('src/app/surveys/page.tsx');
const controlBar = read('src/components/surveys/ControlBar.tsx');
const surveysView = read('src/components/surveys/SurveysView.tsx');
const chartView = read('src/components/surveys/ChartView.tsx');
const plotA = read('src/components/surveys/PlotA.tsx');
const plotB = read('src/components/surveys/PlotB.tsx');
const bandSpectrumStrip = read('src/components/surveys/BandSpectrumStrip.tsx');
const surveyCard = read('src/components/surveys/SurveyCard.tsx');
const filterSheet = read('src/components/surveys/FilterSheet.tsx');
const surveyPeek = read('src/components/surveys/SurveyPeek.tsx');
const surveyDetailClient = read('src/app/surveys/[slug]/SurveyDetailClient.tsx');
const plottingPath = path('src/components/surveys/plotting.ts');
const plotting = existsSync(plottingPath) ? readFileSync(plottingPath, 'utf8') : '';

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
assert.match(chartView, /import PlotB from "\.\/PlotB"/, 'ChartView should import PlotB for the depth-vs-breadth plot.');
assert.match(chartView, /statusOpSurveys: Survey\[\]/, 'ChartView should accept status/operator filtered rows for PlotB so non-band rows can dim instead of disappear.');
assert.match(chartView, /<PlotB[\s\S]*surveys=\{statusOpSurveys\}/, 'ChartView should render PlotB with status/operator filtered rows.');

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

assert.match(plotB, /role="img"/, 'PlotB SVG should expose image semantics.');
assert.match(plotB, /aria-labelledby/, 'PlotB SVG should link to an accessible title/description.');
assert.match(plotB, /<title id=\{titleId\}>/, 'PlotB should include an SVG title.');
assert.match(plotB, /<desc id=\{descId\}>/, 'PlotB should include an SVG description.');
assert.match(plotB, /role="button"/, 'PlotB points should be keyboard-reachable buttons.');
assert.match(plotB, /tabIndex=\{0\}/, 'PlotB points should be tabbable.');
assert.match(plotB, /onKeyDown=\{\(event\) =>/, 'PlotB points should handle keyboard activation.');
assert.match(plotB, /aria-expanded=\{missingExpanded\}/, 'PlotB not-shown disclosure should expose aria-expanded state.');
assert.match(plotB, /aria-controls=\{missingListId\}/, 'PlotB not-shown disclosure should point at its controlled region.');
assert.match(plotB, /id=\{missingListId\}/, 'PlotB not-shown region should expose the ID referenced by aria-controls.');
assert.match(plotB, /s\.num_sources_count > 0/, 'PlotB log-scale source-count axis should reject zero and negative counts.');

assert.ok(existsSync(plottingPath), 'Plotting helpers should live in a shared plotting.ts module.');
assert.match(plotting, /export const AXIS_OPTIONS/, 'Axis options should be exported from shared plotting helpers.');
assert.match(plotting, /export function getSurveyAxisValue/, 'Shared plotting helpers should expose the axis-value conversion function.');
assert.match(plotting, /export function surveyHasPlottableAxes/, 'Shared plotting helpers should expose the plottability predicate.');
assert.match(plotting, /export function parseAxisParam/, 'Shared plotting helpers should validate URL axis params with a fallback.');
assert.match(surveysView, /function parseBandParam/, 'SurveysView should validate URL band params before storing reducer state.');
assert.match(surveysView, /function parseStatusesParam/, 'SurveysView should validate URL status params before storing reducer state.');
assert.match(surveysView, /function parsePlotTypeParam/, 'SurveysView should validate URL plot type params before storing reducer state.');
assert.match(surveysView, /band: parseBandParam\(params\.get\("band"\)\)/, 'Initial band should validate malformed URL params before storing reducer state.');
assert.match(surveysView, /checkedStatuses: parseStatusesParam\(statusesParam\)/, 'Initial statuses should validate malformed URL params before storing reducer state.');
assert.match(surveysView, /plotType: parsePlotTypeParam\(params\.get\("plottype"\)\)/, 'Initial plot type should validate malformed URL params before storing reducer state.');
assert.doesNotMatch(surveysView, /params\.get\("band"\) as BandId/, 'Band URL param should not be blindly cast.');
assert.doesNotMatch(surveysView, /params\.get\("plottype"\) as any/, 'Plot type URL param should not be blindly cast.');
assert.match(surveysView, /parseAxisParam\(params\.get\("xaxis"\), "wavelength_center_um"\)/, 'Initial xAxis should validate malformed URL params before storing reducer state.');
assert.match(surveysView, /parseAxisParam\(params\.get\("yaxis"\), "z_max"\)/, 'Initial yAxis should validate malformed URL params before storing reducer state.');
assert.match(chartView, /from "\.\/plotting"/, 'ChartView should import shared plotting helpers.');
assert.match(plotA, /from "\.\/plotting"/, 'PlotA should import shared plotting helpers.');
assert.doesNotMatch(chartView, /function isPlottable/, 'ChartView should not keep a private plottability predicate.');
assert.match(surveysView, /statusOpSurveys=\{statusOpSurveys\}/, 'SurveysView should pass status/operator filtered rows to ChartView for PlotB.');

assert.match(bandSpectrumStrip, /<button[\s\S]*type="button"/, 'BandSpectrumStrip segments should use native buttons.');
assert.match(bandSpectrumStrip, /aria-pressed=\{active\}/, 'BandSpectrumStrip band buttons should expose selected state.');
assert.match(bandSpectrumStrip, /disabled=\{count === 0\}/, 'Empty BandSpectrumStrip band buttons should be disabled, not pointer-event-only divs.');
assert.match(surveyCard, /<button[\s\S]*className="survey-card"/, 'SurveyCard should use a native button for opening the peek panel.');
assert.match(surveyCard, /aria-label=\{`Open \$\{survey\.name\} survey details`\}/, 'SurveyCard button should have an explicit accessible label.');
assert.match(filterSheet, /role="dialog"/, 'FilterSheet should expose dialog semantics.');
assert.match(filterSheet, /aria-modal="true"/, 'FilterSheet should expose modal semantics.');
assert.match(surveyPeek, /role="dialog"/, 'SurveyPeek should expose dialog semantics.');
assert.match(surveyPeek, /aria-modal="true"/, 'SurveyPeek should expose modal semantics.');
assert.match(surveyDetailClient, /aria-expanded=\{open\}/, 'Dataset catalog disclosure buttons should expose aria-expanded state.');
assert.match(surveyDetailClient, /aria-controls=\{fieldPanelId\}/, 'Dataset catalog disclosure buttons should point at their controlled panel.');
assert.match(surveyDetailClient, /id=\{fieldPanelId\}/, 'Dataset catalog field panels should expose IDs referenced by aria-controls.');

console.log('surveys atlas IA smoke checks passed');
