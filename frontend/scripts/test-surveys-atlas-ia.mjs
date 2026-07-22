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
const plotB = read('src/components/surveys/PlotB.tsx');
const surveyCard = read('src/components/surveys/SurveyCard.tsx');
const bandSpectrumStrip = read('src/components/surveys/BandSpectrumStrip.tsx');
const filterSheet = read('src/components/surveys/FilterSheet.tsx');
const surveyPeek = read('src/components/surveys/SurveyPeek.tsx');
const surveyDetailClient = read('src/app/surveys/[slug]/SurveyDetailClient.tsx');
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

function parseTypeScript(source, fileName) {
  return ts.createSourceFile(path(fileName), source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
}

function findFunctionDeclaration(source, fileName, functionName) {
  const sourceFile = parseTypeScript(source, fileName);
  return {
    sourceFile,
    declaration: sourceFile.statements.find(
      statement => ts.isFunctionDeclaration(statement) && statement.name?.text === functionName,
    ),
  };
}

function hasExactSearchStatusOpInitialization(source, fileName) {
  const sourceFile = parseTypeScript(source, fileName);
  let initializer = null;
  function visit(node) {
    if (
      ts.isVariableDeclaration(node)
      && ts.isIdentifier(node.name)
      && node.name.text === 'searchStatusOpSurveys'
    ) {
      initializer = node.initializer ?? null;
      return;
    }
    ts.forEachChild(node, visit);
  }
  visit(sourceFile);
  if (!initializer) return false;

  let searchCall = initializer;
  if (
    ts.isCallExpression(initializer)
    && initializer.expression.getText(sourceFile) === 'useMemo'
  ) {
    const [factory, dependencies] = initializer.arguments;
    if (
      !factory
      || !ts.isArrowFunction(factory)
      || !ts.isCallExpression(factory.body)
      || !dependencies
      || !ts.isArrayLiteralExpression(dependencies)
      || dependencies.elements.length !== 2
      || dependencies.elements[0].getText(sourceFile) !== 'statusOpSurveys'
      || dependencies.elements[1].getText(sourceFile) !== 'state.search'
    ) {
      return false;
    }
    searchCall = factory.body;
  }

  return ts.isCallExpression(searchCall)
    && searchCall.expression.getText(sourceFile) === 'filterSurveysBySearch'
    && searchCall.arguments.length === 2
    && searchCall.arguments[0].getText(sourceFile) === 'statusOpSurveys'
    && searchCall.arguments[1].getText(sourceFile) === 'state.search';
}

function evaluateStandaloneFunction(source, fileName, functionName) {
  const { sourceFile, declaration } = findFunctionDeclaration(source, fileName, functionName);
  assert.ok(declaration, `${functionName} should be declared as an extractable pure function.`);
  const compiled = ts.transpileModule(declaration.getText(sourceFile), {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2019,
      strict: true,
    },
    fileName: path(fileName),
  });
  const isolatedModule = { exports: {} };
  vm.runInNewContext(
    compiled.outputText,
    { module: isolatedModule, exports: isolatedModule.exports },
    { filename: path(fileName) },
  );
  return isolatedModule.exports[functionName];
}

function findJsxAttributeExpression(source, fileName, tagName, attributeName) {
  const sourceFile = parseTypeScript(source, fileName);
  let expression = null;
  function visit(node) {
    if (
      (ts.isJsxSelfClosingElement(node) || ts.isJsxOpeningElement(node))
      && node.tagName.getText(sourceFile) === tagName
    ) {
      const attribute = node.attributes.properties.find(
        property => ts.isJsxAttribute(property) && property.name.getText(sourceFile) === attributeName,
      );
      if (attribute && ts.isJsxAttribute(attribute) && attribute.initializer && ts.isJsxExpression(attribute.initializer)) {
        expression = attribute.initializer.expression?.getText(sourceFile) ?? null;
      } else if (attribute && ts.isJsxAttribute(attribute) && attribute.initializer && ts.isStringLiteral(attribute.initializer)) {
        expression = attribute.initializer.text;
      }
    }
    ts.forEachChild(node, visit);
  }
  visit(sourceFile);
  return expression;
}

function inspectDatasetCardStructure(source) {
  const fileName = 'src/app/surveys/[slug]/SurveyDetailClient.tsx';
  const sourceFile = parseTypeScript(source, fileName);
  const datasetCard = sourceFile.statements.find(
    statement => ts.isFunctionDeclaration(statement) && statement.name?.text === 'DatasetCard',
  );
  assert.ok(datasetCard, 'DatasetCard should remain a function declaration that can be structurally inspected.');

  const attributeValue = (opening, attributeName) => {
    const attribute = opening.attributes.properties.find(
      property => ts.isJsxAttribute(property) && property.name.getText(sourceFile) === attributeName,
    );
    if (!attribute || !ts.isJsxAttribute(attribute) || !attribute.initializer) return null;
    if (ts.isStringLiteral(attribute.initializer)) return attribute.initializer.text;
    if (ts.isJsxExpression(attribute.initializer)) return attribute.initializer.expression?.getText(sourceFile) ?? null;
    return null;
  };

  let disclosureButton = null;
  let dataLink = null;
  let fieldPanel = null;
  function visit(node) {
    if (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node)) {
      const tagName = node.tagName.getText(sourceFile);
      if (tagName === 'button' && attributeValue(node, 'aria-controls') === 'fieldPanelId') disclosureButton = node;
      if (tagName === 'a' && attributeValue(node, 'href') === 'dataset.primary_url') dataLink = node;
      if (tagName === 'div' && attributeValue(node, 'id') === 'fieldPanelId') fieldPanel = node;
    }
    ts.forEachChild(node, visit);
  }
  visit(datasetCard);

  assert.ok(disclosureButton, 'DatasetCard should expose a disclosure button controlling fieldPanelId.');
  assert.ok(dataLink, 'DatasetCard should expose its primary Data link.');
  assert.ok(fieldPanel, 'DatasetCard should keep the fieldPanelId region in its TSX tree.');

  const disclosureElement = disclosureButton.parent;
  const dataLinkElement = dataLink.parent;
  const fieldPanelElement = fieldPanel.parent;
  const nearestJsxParent = (node) => {
    let current = node.parent;
    while (current && current !== datasetCard) {
      if (ts.isJsxElement(current) || ts.isJsxSelfClosingElement(current)) return current;
      current = current.parent;
    }
    return null;
  };
  let linkInsideButton = false;
  for (let current = dataLinkElement.parent; current && current !== datasetCard; current = current.parent) {
    if (ts.isJsxElement(current) && current.openingElement.tagName.getText(sourceFile) === 'button') {
      linkInsideButton = true;
      break;
    }
  }
  let panelConditionallyMounted = false;
  for (let current = fieldPanelElement.parent; current && current !== datasetCard; current = current.parent) {
    if (
      ts.isBinaryExpression(current)
      && current.operatorToken.kind === ts.SyntaxKind.AmpersandAmpersandToken
      && current.left.getText(sourceFile).includes('open')
    ) {
      panelConditionallyMounted = true;
      break;
    }
  }

  return {
    buttonType: attributeValue(disclosureButton, 'type'),
    buttonExpanded: attributeValue(disclosureButton, 'aria-expanded'),
    buttonControls: attributeValue(disclosureButton, 'aria-controls'),
    panelId: attributeValue(fieldPanel, 'id'),
    panelHidden: attributeValue(fieldPanel, 'hidden'),
    panelConditionallyMounted,
    linkInsideButton,
    linkAndButtonAreSiblings: nearestJsxParent(disclosureElement) === nearestJsxParent(dataLinkElement),
  };
}

function inspectInteractivePlotStructure(source, fileName) {
  const sourceFile = parseTypeScript(source, fileName);
  const attributeValue = (opening, attributeName) => {
    const attribute = opening.attributes.properties.find(
      property => ts.isJsxAttribute(property) && property.name.getText(sourceFile) === attributeName,
    );
    if (!attribute || !ts.isJsxAttribute(attribute) || !attribute.initializer) return null;
    if (ts.isStringLiteral(attribute.initializer)) return attribute.initializer.text;
    if (ts.isJsxExpression(attribute.initializer)) return attribute.initializer.expression?.getText(sourceFile) ?? null;
    return null;
  };

  let plotSvg = null;
  function findPlotSvg(node) {
    if (
      ts.isJsxOpeningElement(node)
      && node.tagName.getText(sourceFile) === 'svg'
      && attributeValue(node, 'aria-labelledby') !== null
    ) {
      plotSvg = node;
      return;
    }
    ts.forEachChild(node, findPlotSvg);
  }
  findPlotSvg(sourceFile);
  assert.ok(plotSvg, `${fileName} should expose an SVG with aria-labelledby.`);

  let interactivePoint = null;
  function findInteractivePoint(node) {
    if (
      (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node))
      && node.tagName.getText(sourceFile) === 'g'
      && attributeValue(node, 'role') === 'button'
    ) {
      interactivePoint = node;
      return;
    }
    ts.forEachChild(node, findInteractivePoint);
  }
  findInteractivePoint(plotSvg.parent);
  assert.ok(interactivePoint, `${fileName} should keep interactive point descendants in its labelled SVG.`);

  return {
    containerRole: attributeValue(plotSvg, 'role'),
    containerLabelledBy: attributeValue(plotSvg, 'aria-labelledby'),
    pointRole: attributeValue(interactivePoint, 'role'),
    pointTabIndex: attributeValue(interactivePoint, 'tabIndex'),
  };
}

function inspectFilterDialogRelationship(controlBarSource, filterSheetSource) {
  const controlFileName = 'src/components/surveys/ControlBar.tsx';
  const filterFileName = 'src/components/surveys/FilterSheet.tsx';
  const controlSourceFile = parseTypeScript(controlBarSource, controlFileName);
  const filterSourceFile = parseTypeScript(filterSheetSource, filterFileName);
  const attributeValue = (opening, attributeName, sourceFile) => {
    const attribute = opening.attributes.properties.find(
      property => ts.isJsxAttribute(property) && property.name.getText(sourceFile) === attributeName,
    );
    if (!attribute || !ts.isJsxAttribute(attribute) || !attribute.initializer) return null;
    if (ts.isStringLiteral(attribute.initializer)) return attribute.initializer.text;
    if (ts.isJsxExpression(attribute.initializer)) return attribute.initializer.expression?.getText(sourceFile) ?? null;
    return null;
  };

  let trigger = null;
  function findTrigger(node) {
    if (
      (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node))
      && node.tagName.getText(controlSourceFile) === 'button'
      && attributeValue(node, 'aria-label', controlSourceFile) === 'Open survey filters'
    ) {
      trigger = node;
      return;
    }
    ts.forEachChild(node, findTrigger);
  }
  findTrigger(controlSourceFile);
  assert.ok(trigger, 'ControlBar should expose the filter-dialog trigger.');

  let dialog = null;
  function findDialog(node) {
    if (
      (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node))
      && node.tagName.getText(filterSourceFile) === 'div'
      && attributeValue(node, 'id', filterSourceFile) === 'surveys-filter-sheet'
    ) {
      dialog = node;
      return;
    }
    ts.forEachChild(node, findDialog);
  }
  findDialog(filterSourceFile);
  assert.ok(dialog, 'FilterSheet should keep the dialog target in its open branch.');

  return {
    triggerHasPopup: attributeValue(trigger, 'aria-haspopup', controlSourceFile),
    triggerExpanded: attributeValue(trigger, 'aria-expanded', controlSourceFile),
    triggerControls: attributeValue(trigger, 'aria-controls', controlSourceFile),
    dialogId: attributeValue(dialog, 'id', filterSourceFile),
    dialogRole: attributeValue(dialog, 'role', filterSourceFile),
    dialogModal: attributeValue(dialog, 'aria-modal', filterSourceFile),
  };
}

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
assert.match(controlBar, /filterSheetOpen: boolean/, 'ControlBar should accept filter sheet open state for aria-expanded.');
assert.match(controlBar, /aria-haspopup="dialog"/, 'Filter trigger should announce that it opens a dialog.');
assert.match(controlBar, /aria-expanded=\{filterSheetOpen\}/, 'Filter trigger should expose dialog open state.');
assert.match(surveysView, /filterSheetOpen=\{filterSheetOpen\}/, 'SurveysView should pass filter sheet open state to ControlBar.');
const filterDialogRelationship = inspectFilterDialogRelationship(controlBar, filterSheet);
assert.deepEqual(
  filterDialogRelationship,
  {
    triggerHasPopup: 'dialog',
    triggerExpanded: 'filterSheetOpen',
    triggerControls: 'filterSheetOpen ? "surveys-filter-sheet" : undefined',
    dialogId: 'surveys-filter-sheet',
    dialogRole: 'dialog',
    dialogModal: 'true',
  },
  'The filter trigger should reference its conditionally mounted dialog only while that dialog is open.',
);
assert.match(filterSheet, /aria-labelledby="surveys-filter-sheet-title"/, 'FilterSheet should label the dialog by its title.');
assert.match(filterSheet, /id="surveys-filter-sheet-title"/, 'FilterSheet title should expose the label ID.');
assert.match(surveyPeek, /role="dialog"/, 'SurveyPeek should use dialog semantics.');
assert.match(surveyPeek, /aria-modal="true"/, 'SurveyPeek should expose modal semantics.');
assert.match(surveyPeek, /aria-label=\{`\$\{survey\.name\} survey details`\}/, 'SurveyPeek should expose a descriptive dialog label.');

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

assert.equal(
  hasExactSearchStatusOpInitialization(
    'const searchStatusOpSurveys = statusOpSurveys;',
    'fixtures/search-bypass.ts',
  ),
  false,
  'The B1 AST checker should reject the original search bypass.',
);
assert.equal(
  hasExactSearchStatusOpInitialization(
    'const searchStatusOpSurveys = filterSurveysBySearch(statusOpSurveys.filter(survey => survey.wavelength_band === state.band), state.search);',
    'fixtures/search-band-filter.ts',
  ),
  false,
  'The B1 AST checker should reject applying a band filter before PlotB search filtering.',
);
assert.equal(
  hasExactSearchStatusOpInitialization(
    'const searchStatusOpSurveys = filterSurveysBySearch(statusOpSurveys, state.search);',
    'fixtures/search-correct.ts',
  ),
  true,
  'The B1 AST checker should accept the exact search+status+operator initialization.',
);
assert.equal(
  hasExactSearchStatusOpInitialization(surveysView, 'src/components/surveys/SurveysView.tsx'),
  true,
  'SurveysView should initialize PlotB rows from search over the status+operator set, before band filtering.',
);

const filterSurveysBySearch = evaluateStandaloneFunction(
  surveysView,
  'src/components/surveys/SurveysView.tsx',
  'filterSurveysBySearch',
);
const plotBSearchFixture = [
  { slug: 'kept-active-band', name: 'Deep Alpha', full_name: 'Deep Alpha Survey', operator: 'Op A', primary_science_goals: 'Cosmology', wavelength_band: 'optical' },
  { slug: 'excluded-search-miss', name: 'Wide Beta', full_name: 'Wide Beta Survey', operator: 'Op A', primary_science_goals: 'Cosmology', wavelength_band: 'optical' },
  { slug: 'kept-outside-band', name: 'Deep Gamma', full_name: 'Deep Gamma Survey', operator: 'Op A', primary_science_goals: 'Cosmology', wavelength_band: 'radio' },
];
assert.deepEqual(
  Array.from(filterSurveysBySearch(plotBSearchFixture, 'deep'), survey => survey.slug),
  ['kept-active-band', 'kept-outside-band'],
  'PlotB search filtering should exclude search misses while preserving matching rows outside the selected band.',
);
assert.equal(
  findJsxAttributeExpression(surveysView, 'src/components/surveys/SurveysView.tsx', 'ChartView', 'plotBSurveys'),
  'searchStatusOpSurveys',
  'SurveysView should pass search+status+operator rows, without a band filter, to ChartView for PlotB.',
);
assert.equal(
  findJsxAttributeExpression(chartView, 'src/components/surveys/ChartView.tsx', 'PlotB', 'surveys'),
  'plotBSurveys',
  'ChartView should pass the search+status+operator PlotB set to PlotB.',
);
assert.match(
  chartView,
  /\{plotBSurveys\.length\} matching search, status, and operator filters/,
  'The PlotB card should report the count for the same search+status+operator set that it renders.',
);

assert.match(plotA, /aria-labelledby/, 'Plot SVG should link to an accessible title/description.');
assert.match(plotA, /aria-expanded=\{missingExpanded\}/, 'Not-plotted disclosure button should expose aria-expanded state.');
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
const plotAStructure = inspectInteractivePlotStructure(plotA, 'src/components/surveys/PlotA.tsx');
assert.deepEqual(
  plotAStructure,
  {
    containerRole: 'group',
    containerLabelledBy: '`${titleId} ${descId}`',
    pointRole: 'button',
    pointTabIndex: '0',
  },
  'PlotA should expose labelled interactive-group semantics without flattening its focusable button points.',
);

const surveyHasPlotBData = evaluateStandaloneFunction(
  plotB,
  'src/components/surveys/PlotB.tsx',
  'surveyHasPlotBData',
);
assert.equal(surveyHasPlotBData({ num_sources_count: 42, limiting_magnitude: 24.1 }), true, 'PlotB should accept positive source counts with a limiting magnitude.');
assert.equal(surveyHasPlotBData({ num_sources_count: 0, limiting_magnitude: 24.1 }), false, 'PlotB should reject zero source counts for its logarithmic axis.');
assert.equal(surveyHasPlotBData({ num_sources_count: -4, limiting_magnitude: 24.1 }), false, 'PlotB should reject negative source counts for its logarithmic axis.');
assert.equal(surveyHasPlotBData({ num_sources_count: null, limiting_magnitude: 24.1 }), false, 'PlotB should reject missing source counts.');
assert.equal(surveyHasPlotBData({ num_sources_count: 42, limiting_magnitude: null }), false, 'PlotB should reject missing limiting magnitudes.');
assert.match(plotB, /const renderMissingSurveys = \(\) => \(/, 'PlotB should centralize its not-shown disclosure for plotted and zero-plotted states.');
assert.match(
  plotB,
  /getPlotBEmptyMessage\(surveys\.length\)[\s\S]*renderMissingSurveys\(\)/,
  'When filters match surveys but zero PlotB points are plottable, the not-shown disclosure should remain visible.',
);
const getPlotBEmptyMessage = evaluateStandaloneFunction(
  plotB,
  'src/components/surveys/PlotB.tsx',
  'getPlotBEmptyMessage',
);
assert.equal(
  getPlotBEmptyMessage(0),
  'No surveys match the active search, status, and operator filters.',
  'PlotB should truthfully describe a filter-empty dataset without claiming ingestion has not happened.',
);
assert.equal(
  getPlotBEmptyMessage(1),
  '1 matching survey, but none have positive source counts and limiting magnitude values.',
  'PlotB should distinguish matched-but-unplottable rows from a filter-empty dataset.',
);
assert.doesNotMatch(plotB, /populated by Mima/, 'PlotB should not infer an ingestion state from a filtered-empty dataset.');
assert.match(plotB, /none have positive source counts and limiting magnitude values/, 'PlotB should explain why matching surveys produced zero points.');
assert.match(plotB, /useId/, 'PlotB should generate stable IDs for its accessible SVG name and description.');
assert.equal(
  findJsxAttributeExpression(plotB, 'src/components/surveys/PlotB.tsx', 'svg', 'role'),
  'group',
  'PlotB should use group semantics so its interactive point descendants remain exposed.',
);
assert.equal(
  findJsxAttributeExpression(plotB, 'src/components/surveys/PlotB.tsx', 'svg', 'aria-labelledby'),
  '`${titleId} ${descId}`',
  'PlotB interactive SVG group should retain its title/description relationship.',
);
assert.equal(
  findJsxAttributeExpression(plotB, 'src/components/surveys/PlotB.tsx', 'g', 'role'),
  'button',
  'PlotB point groups should remain exposed as interactive buttons.',
);
assert.equal(
  findJsxAttributeExpression(plotB, 'src/components/surveys/PlotB.tsx', 'g', 'tabIndex'),
  '0',
  'PlotB point buttons should remain in the keyboard tab order.',
);
assert.match(plotB, /aria-labelledby=\{`\$\{titleId\} \$\{descId\}`\}/, 'PlotB SVG should reference its title and description IDs.');
assert.match(plotB, /<title id=\{titleId\}>/, 'PlotB should include an SVG title.');
assert.match(plotB, /<desc id=\{descId\}>/, 'PlotB should include an SVG description.');
assert.match(plotB, /role="button"/, 'PlotB points should expose button semantics.');
assert.match(plotB, /tabIndex=\{0\}/, 'PlotB points should be keyboard reachable.');
assert.match(plotB, /onFocus=\{\(\) => onHover\(s\.slug\)\}/, 'PlotB points should share their hover highlight when focused.');
assert.match(plotB, /onBlur=\{\(\) => onHover\(null\)\}/, 'PlotB points should clear their highlight when focus leaves.');
assert.match(plotB, /onKeyDown=\{\(event\) =>/, 'PlotB points should handle keyboard activation.');
assert.match(plotB, /event\.key === "Enter" \|\| event\.key === " "/, 'PlotB points should activate on Enter or Space.');
assert.match(plotB, /aria-label=\{`Open \$\{s\.name\} survey details`\}/, 'PlotB points should announce the survey they open.');
assert.match(plotB, /const missingListId = useId\(\)/, 'PlotB should generate an ID for its missing-data region.');
assert.match(plotB, /type="button"/, 'PlotB missing-data disclosure should not submit an enclosing form.');
assert.match(plotB, /aria-expanded=\{missingExpanded\}/, 'PlotB missing-data disclosure should expose expanded state.');
assert.match(plotB, /aria-controls=\{missingListId\}/, 'PlotB missing-data disclosure should reference its controlled region.');
assert.match(plotB, /id=\{missingListId\}/, 'PlotB missing-data region should expose the referenced ID.');

function inspectMissingDisclosure(source, fileName, componentName) {
  const sourceFile = parseTypeScript(source, fileName);
  const attributeValue = (opening, attributeName) => {
    const attribute = opening.attributes.properties.find(
      property => ts.isJsxAttribute(property) && property.name.getText(sourceFile) === attributeName,
    );
    if (!attribute || !ts.isJsxAttribute(attribute) || !attribute.initializer) return null;
    if (ts.isStringLiteral(attribute.initializer)) return attribute.initializer.text;
    if (ts.isJsxExpression(attribute.initializer)) return attribute.initializer.expression?.getText(sourceFile) ?? null;
    return null;
  };
  let disclosureButton = null;
  let disclosurePanel = null;
  function visit(node) {
    if (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node)) {
      const tagName = node.tagName.getText(sourceFile);
      if (tagName === 'button' && attributeValue(node, 'aria-controls') === 'missingListId') disclosureButton = node;
      if (tagName === 'div' && attributeValue(node, 'id') === 'missingListId') disclosurePanel = node;
    }
    ts.forEachChild(node, visit);
  }
  visit(sourceFile);
  assert.ok(disclosureButton, `${componentName} should expose its missing-data disclosure button.`);
  assert.ok(disclosurePanel, `${componentName} should expose the controlled missing-data panel.`);

  let panelConditionallyMounted = false;
  for (let current = disclosurePanel.parent; current && current !== sourceFile; current = current.parent) {
    if (
      ts.isBinaryExpression(current)
      && current.operatorToken.kind === ts.SyntaxKind.AmpersandAmpersandToken
      && current.left.getText(sourceFile).includes('missingExpanded')
    ) {
      panelConditionallyMounted = true;
      break;
    }
  }
  return {
    buttonControls: attributeValue(disclosureButton, 'aria-controls'),
    panelId: attributeValue(disclosurePanel, 'id'),
    panelHidden: attributeValue(disclosurePanel, 'hidden'),
    panelConditionallyMounted,
  };
}

const plotAMissingDisclosure = inspectMissingDisclosure(
  plotA,
  'src/components/surveys/PlotA.tsx',
  'PlotA',
);
assert.deepEqual(
  plotAMissingDisclosure,
  {
    buttonControls: 'missingListId',
    panelId: 'missingListId',
    panelHidden: '!missingExpanded',
    panelConditionallyMounted: false,
  },
  'PlotA missing-data disclosure should control an always-mounted region hidden while collapsed.',
);

const plotBMissingDisclosure = inspectMissingDisclosure(
  plotB,
  'src/components/surveys/PlotB.tsx',
  'PlotB',
);
assert.deepEqual(
  plotBMissingDisclosure,
  {
    buttonControls: 'missingListId',
    panelId: 'missingListId',
    panelHidden: '!missingExpanded',
    panelConditionallyMounted: false,
  },
  'PlotB missing-data disclosure should control an always-mounted region hidden while collapsed.',
);

const datasetCardStructure = inspectDatasetCardStructure(surveyDetailClient);
assert.deepEqual(
  {
    buttonType: datasetCardStructure.buttonType,
    buttonExpanded: datasetCardStructure.buttonExpanded,
    buttonControls: datasetCardStructure.buttonControls,
    panelId: datasetCardStructure.panelId,
    panelHidden: datasetCardStructure.panelHidden,
  },
  {
    buttonType: 'button',
    buttonExpanded: 'open',
    buttonControls: 'fieldPanelId',
    panelId: 'fieldPanelId',
    panelHidden: '!open',
  },
  'DatasetCard disclosure state should map to an always-mounted, hidden controlled panel.',
);
assert.equal(datasetCardStructure.panelConditionallyMounted, false, 'DatasetCard controlled panel should not be conditionally unmounted.');
assert.equal(datasetCardStructure.linkInsideButton, false, 'DatasetCard Data link should never be nested inside the disclosure button.');
assert.equal(datasetCardStructure.linkAndButtonAreSiblings, true, 'DatasetCard Data link and disclosure button should be direct siblings.');

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
