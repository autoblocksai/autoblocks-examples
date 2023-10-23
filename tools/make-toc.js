const fs = require('fs/promises');

const makeMarkdownTable = (headers, rows) => {
  const columnWidths = [headers, ...rows].reduce((acc, row) => {
    return row.map((cell, i) => Math.max(acc[i] || 0, cell.length));
  }, []);
  const headerSeparator = columnWidths.map((width) => '-'.repeat(width));
  const table = [headers, headerSeparator, ...rows];
  return table.map((row) => {
    return `| ${row.map((cell, i) => cell.padEnd(columnWidths[i])).join(' | ')} |`;
  }).join('\n');
};

const replaceContentBetweenComments = ({ content, startComment, endComment, replacement }) => {
  const startIdx = content.indexOf(startComment) + startComment.length;
  const endIdx = content.indexOf(endComment);
  return `${content.slice(0, startIdx)}\n${replacement}\n${content.slice(endIdx)}`;
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

// Reminder we add below the banner to each individual project README
const GETTING_STARTED_REMINDER = `<p align="center">
  :bangbang:
  Make sure you've read the <a href="/README.md#getting-started">getting started</a> section in the main README.
</p>`;

const BANNER_START_COMMENT = '<!-- banner start -->';
const BANNER_END_COMMENT = '<!-- banner end -->';

(async function () {
  let readme = await fs.readFile('README.md', 'utf-8');

  const headers = ['Name', 'Description'];

  for (const section of ['JavaScript', 'Python']) {
    const rows = [];
    const projects = await fs.readdir(section);

    for (const project of projects) {
      let description;

      if (section === 'JavaScript') {
        // Get description from package.json
        const packageJson = await fs.readFile(`${section}/${project}/package.json`, 'utf-8');
        description = JSON.parse(packageJson).description;
      } else if (section === 'Python') {
        // Get description from pyproject.toml
        const pyprojectToml = await fs.readFile(`${section}/${project}/pyproject.toml`, 'utf-8');
        description = pyprojectToml.match(/description = "(.*)"/)[1];
      }

      // Add name and description to table
      rows.push([`[${project}](/${section}/${project})`, description]);

      let projectReadme = await fs.readFile(`${section}/${project}/README.md`, 'utf-8');
      
      // Add banner + getting started reminder to top of project README
      projectReadme = replaceContentBetweenComments({
        content: projectReadme,
        startComment: BANNER_START_COMMENT,
        endComment: BANNER_END_COMMENT,
        replacement: [BANNER, GETTING_STARTED_REMINDER].join('\n'),
      });

      // Write the new project README
      await fs.writeFile(`${section}/${project}/README.md`, projectReadme);
    }

    // Add the table of projects to the main README
    readme = replaceContentBetweenComments({
      content: readme,
      startComment: `<!-- ${section} start -->`,
      endComment: `<!-- ${section} end -->`,
      replacement: makeMarkdownTable(headers, rows),
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
