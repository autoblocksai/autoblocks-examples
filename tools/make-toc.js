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

// Text we add to the top of each individual README
const BANNER = `<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
</p>

<p align="center">
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  |
  <a href="https://app.autoblocks.ai/">Application</a>
  |
  <a href="https://www.autoblocks.ai/">Home</a>
</p>

<p align="center">
  :bangbang:
  Make sure you've read the <a href="/README.md#getting-started">getting started</a> section in the main README.
</p>`;

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

      // Add banner to top of README
      let projectReadme = await fs.readFile(`${section}/${project}/README.md`, 'utf-8');

      // Find start and end of banner in project README
      const startComment = '<!-- banner start -->';
      const endComment = '<!-- banner end -->';
      const startIdx = projectReadme.indexOf(startComment) + startComment.length;
      const endIdx = projectReadme.indexOf(endComment);

      // Replace the content between the comments with the banner
      projectReadme = `${projectReadme.slice(0, startIdx)}\n${BANNER}\n${projectReadme.slice(endIdx)}`;
      
      // Write the new project README
      await fs.writeFile(`${section}/${project}/README.md`, projectReadme);
    }

    const table = makeMarkdownTable(headers, rows);

    // Look for comments that looks like "<!-- {section} start -->" and "<!-- {section} end -->"
    const startComment = `<!-- ${section} start -->`;
    const endComment = `<!-- ${section} end -->`;
    const startIdx = readme.indexOf(startComment) + startComment.length;
    const endIdx = readme.indexOf(endComment);

    // Replace the content between the comments with the table in the README
    readme = `${readme.slice(0, startIdx)}\n${table}\n${readme.slice(endIdx)}`;
  }

  // Write the new README
  await fs.writeFile('README.md', readme);
})();
