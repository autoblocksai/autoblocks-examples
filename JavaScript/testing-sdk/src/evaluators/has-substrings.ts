import { BaseTestEvaluator, type Threshold } from '@autoblocks/client/testing';

export abstract class BaseHasSubstrings<T, O> extends BaseTestEvaluator<T, O> {
  id = 'has-substrings';

  /**
   * Subclasses should implement this method to return the expected substrings
   * for the given test case and output.
   *
   * Both the test case and output are made available to the subclass to
   * accommodate scenarios where the expected substrings are derived from:
   *
   * - The test case
   * - The output
   * - Both
   */
  abstract expectedSubstrings(args: { testCase: T; output: O }): string[];

  /**
   * Subclasses should implement this method to convert the output to a string.
   */
  abstract outputAsString(output: O): string;

  evaluateTestCase(args: { testCase: T; output: O }) {
    const expectedSubstrings = this.expectedSubstrings(args);
    const outputAsStr = this.outputAsString(args.output);
    const score = expectedSubstrings.every((s) => outputAsStr.includes(s))
      ? 1
      : 0;
    return { score, threshold: { gte: 1 } };
  }
}
