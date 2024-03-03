export interface TestCase {
  topic: string;
  expectedSubstrings: string[];
}

export function genTestCases(): TestCase[] {
  return [
    {
      topic: 'Introduction to Organic Chemistry',
      expectedSubstrings: ['Functional Groups'],
    },
    {
      topic: 'Fundamentals of Calculus',
      expectedSubstrings: ['Derivatives', 'Differentiation'],
    },
    {
      topic: 'World History: Ancient Civilizations',
      expectedSubstrings: ['Mesopotamia', 'Egypt'],
    },
    {
      topic: 'Basics of Programming in Python',
      expectedSubstrings: ['Syntax', 'Variables', 'Functions'],
    },
    {
      topic: 'Principles of Economics',
      expectedSubstrings: ['Microeconomics', 'Macroeconomics'],
    },
  ];
}
