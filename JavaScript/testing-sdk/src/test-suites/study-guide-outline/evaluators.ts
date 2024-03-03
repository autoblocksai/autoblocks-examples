import { BaseHasSubstrings } from '../../evaluators/has-substrings';
import { BaseTestEvaluator } from '@autoblocks/client/testing';
import type { TestCase } from './test-cases';

export class Formatting extends BaseTestEvaluator<TestCase, string> {
  id = 'formatting';

  /**
   * Every line should either be blank or start with "* " or "  - "
   */
  score(output: string): number {
    for (const line of output.split('\n')) {
      const conditions: boolean[] = [
        line.trim() === '',
        line.startsWith('* '),
        line.startsWith('  - '),
      ];
      if (!conditions.some((c) => c)) {
        return 0;
      }
    }
    return 1;
  }

  evaluateTestCase(args: { testCase: TestCase; output: string }) {
    return {
      score: this.score(args.output),
      threshold: {
        gte: 1,
      },
    };
  }
}

export class NumCategories extends BaseTestEvaluator<TestCase, string> {
  id = 'num-categories';

  minCategories = 5;
  maxCategories = 10;

  score(output: string): number {
    const numCategories = output
      .split('\n')
      .filter((l) => l.startsWith('* ')).length;
    if (
      numCategories >= this.minCategories &&
      numCategories <= this.maxCategories
    ) {
      return 1;
    }
    return 0;
  }

  evaluateTestCase(args: { testCase: TestCase; output: string }) {
    return {
      score: this.score(args.output),
      threshold: {
        gte: 1,
      },
    };
  }
}

export class HasSubstrings extends BaseHasSubstrings<TestCase, string> {
  id = 'has-substrings';

  expectedSubstrings(args: { testCase: TestCase; output: string }): string[] {
    return args.testCase.expectedSubstrings;
  }

  outputAsString(output: string): string {
    return output;
  }
}
