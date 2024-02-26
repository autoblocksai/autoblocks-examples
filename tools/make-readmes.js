const fs = require('fs/promises');

const makeMarkdownTable = (headers, rows) => {
  const columnWidths = [headers, ...rows].reduce((acc, row) => {
    return row.map((cell, i) => Math.max(acc[i] || 0, cell.length));
  }, []);
  const headerSeparator = columnWidths.map((width) => '-'.repeat(width));
  const table = [headers, headerSeparator, ...rows];
  return table
    .map((row) => {
      return `| ${row
        .map((cell, i) => cell.padEnd(columnWidths[i]))
        .join(' | ')} |`;
    })
    .join('\n');
};

const replaceContentBetweenComments = ({
  content,
  startComment,
  endComment,
  replacement,
}) => {
  const startIdx = content.indexOf(startComment) + startComment.length;
  const endIdx = content.indexOf(endComment);
  if (startIdx !== -1 && endIdx !== -1) {
    return `${content.slice(0, startIdx)}\n${replacement}\n${content.slice(
      endIdx,
    )}`;
  }
  return content;
};

// Banner we add to the top of each README
const BANNER = `<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
</p>

<p align="center">
  📚
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  &nbsp;
  •
  &nbsp;
  🖥️
  <a href="https://app.autoblocks.ai/">Application</a>
  &nbsp;
  •
  &nbsp;
  🏠
  <a href="https://www.autoblocks.ai/">Home</a>
</p>`;

const BANNER_START_COMMENT = '<!-- banner start -->';
const BANNER_END_COMMENT = '<!-- banner end -->';

// Getting started checklist we add to each individual project README
const makeGettingStartedChecklist = ({
  includeOpenAI,
  includeAutoblocksAPIKey,
}) => {
  return `
## Getting started

- Sign up for an Autoblocks account at https://app.autoblocks.ai
- Grab your Autoblocks ingestion key from https://app.autoblocks.ai/settings/api-keys
${
  includeAutoblocksAPIKey
    ? '- Grab your Autoblocks api key from https://app.autoblocks.ai/settings/api-keys'
    : 'DELETE_ME'
}
${
  includeOpenAI
    ? '- Grab your OpenAI API key from https://platform.openai.com/account/api-keys'
    : 'DELETE_ME'
}
- Create a file named \`.env\` in this folder and include the following environment variables:

\`\`\`
${includeOpenAI ? 'OPENAI_API_KEY=<your-api-key>' : 'DELETE_ME'}
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
${includeAutoblocksAPIKey ? 'AUTOBLOCKS_API_KEY=<your-api-key' : 'DELETE_ME'}
\`\`\`
`.replaceAll('DELETE_ME\n', '');
};

const GETTING_STARTED_START_COMMENT = '<!-- getting started start -->';
const GETTING_STARTED_END_COMMENT = '<!-- getting started end -->';

(async function () {
  let readme = await fs.readFile('README.md', 'utf-8');

  const headers = ['Name', 'Description'];

  for (const section of ['JavaScript', 'Python']) {
    const rows = [];
    const projects = await fs.readdir(section);

    for (const project of projects) {
      let description;
      let includeOpenAIInGettingStartedChecklist = false;
      let includeAutoblocksAPIKeyInGettingStartedChecklist = false;

      if (section === 'JavaScript') {
        // Get description from package.json
        const packageJson = await fs.readFile(
          `${section}/${project}/package.json`,
          'utf-8',
        );
        description = JSON.parse(packageJson).description;

        if (
          packageJson.includes('dotenv -e .env -- autoblocks prompts generate')
        ) {
          includeAutoblocksAPIKeyInGettingStartedChecklist = true;
        }

        // Check if openai is a dependency
        if (packageJson.includes('openai')) {
          includeOpenAIInGettingStartedChecklist = true;
        }
      } else if (section === 'Python') {
        // Get description from pyproject.toml
        const pyprojectToml = await fs.readFile(
          `${section}/${project}/pyproject.toml`,
          'utf-8',
        );
        description = pyprojectToml.match(/description = "(.*)"/)[1];

        // Check if openai is a dependency
        if (pyprojectToml.includes('openai')) {
          includeOpenAIInGettingStartedChecklist = true;
        }
      }

      // Add name and description to table
      rows.push([`[${project}](/${section}/${project})`, description]);

      let projectReadme = await fs.readFile(
        `${section}/${project}/README.md`,
        'utf-8',
      );

      // Add banner to top of project README
      projectReadme = replaceContentBetweenComments({
        content: projectReadme,
        startComment: BANNER_START_COMMENT,
        endComment: BANNER_END_COMMENT,
        replacement: BANNER,
      });
      // Add getting started checklist to project README
      projectReadme = replaceContentBetweenComments({
        content: projectReadme,
        startComment: GETTING_STARTED_START_COMMENT,
        endComment: GETTING_STARTED_END_COMMENT,
        replacement: makeGettingStartedChecklist({
          includeOpenAI: includeOpenAIInGettingStartedChecklist,
          includeAutoblocksAPIKey:
            includeAutoblocksAPIKeyInGettingStartedChecklist,
        }),
      });

      // Write the new project README
      await fs.writeFile(`${section}/${project}/README.md`, projectReadme);
    }

    // Add the table of projects to the main README
    readme = replaceContentBetweenComments({
      content: readme,
      startComment: `<!-- ${section} start -->`,
      endComment: `<!-- ${section} end -->`,
      replacement: '\n' + makeMarkdownTable(headers, rows) + '\n',
    });
  }

  // Add banner to main README
  readme = replaceContentBetweenComments({
    content: readme,
    startComment: BANNER_START_COMMENT,
    endComment: BANNER_END_COMMENT,
    replacement: BANNER,
  });

  // Write the new README
  await fs.writeFile('README.md', readme);
})();
