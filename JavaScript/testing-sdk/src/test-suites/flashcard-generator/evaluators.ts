import type { Flashcard } from '../../tasks/flashcard-generator';
import type { TestCase } from './test-cases';
import { BaseTestEvaluator, Evaluation } from '@autoblocks/client/testing';
import OpenAI from 'openai';

const openai = new OpenAI();

export class IsProfessionalTone extends BaseTestEvaluator<
  TestCase,
  Flashcard[]
> {
  id = 'is-professional-tone';

  // Since this evaluator makes calls to an external service (openai),
  // restrict how many evaluations can be made concurrently
  // with this evaluator.
  maxConcurrency = 2;

  prompt = `Please evaluate the provided text for its professionalism in the context of formal communication.
Consider the following criteria in your assessment:

Language Use: Formality, clarity, and precision of language without slang or casual expressions.
Sentence Structure: Logical and well-formed sentence construction without run-ons or fragments.
Tone and Style: Respectful, objective, and appropriately formal tone without bias or excessive emotionality.
Grammar and Punctuation: Correct grammar, punctuation, and capitalization.
Based on these criteria, provide a binary response where:

0 indicates the text does not maintain a professional tone.
1 indicates the text maintains a professional tone.
No further explanation or summary is required; just provide the number that represents your assessment.`;

  async scoreFlashcard(flashcard: Flashcard): Promise<number> {
    const content = `${flashcard.front}\n${flashcard.back}`;

    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo-1106',
      temperature: 0.0,
      n: 1,
      max_tokens: 1,
      messages: [
        {
          role: 'system',
          content: this.prompt,
        },
        {
          role: 'user',
          content: content,
        },
      ],
    });

    const rawContent = response.choices[0].message.content.trim();

    if (rawContent === '0') {
      return 0;
    } else if (rawContent === '1') {
      return 1;
    }

    throw new Error(`Unexpected response: ${rawContent}`);
  }

  async evaluateTestCase(args: {
    testCase: TestCase;
    output: Flashcard[];
  }): Promise<Evaluation> {
    // Score each flashcard asynchronously
    const scores = await Promise.all(
      args.output.map((flashcard) => this.scoreFlashcard(flashcard)),
    );

    if (!scores.length) {
      throw new Error('No scores were returned');
    }

    // Return the average score as the evaluation score
    return { score: scores.reduce((a, b) => a + b, 0) / scores.length };
  }
}

export class IsSupportedByNotes extends BaseTestEvaluator<
  TestCase,
  Flashcard[]
> {
  id = 'is-supported-by-notes';

  // Since this evaluator makes calls to an external service (openai),
  // restrict how many evaluations can be made concurrently
  // with this evaluator.
  maxConcurrency = 2;

  prompt = `Given some notes by a student and a flashcard in the form of a question and answer, evaluate whether the flashcard's question and answer are supported by the notes.
It's possible the question and answer aren't in the notes verbatim.
If the notes provide enough context or information to support the question and answer, consider that sufficient support.
Based on these criteria, provide a binary response where:
0 indicates the flashcard's question and answer are not supported by the notes.
1 indicates the flashcard's question and answer are supported by the notes.
No further explanation or summary is required; just provide the number that represents your assessment.`;

  async scoreFlashcard(args: {
    testCase: TestCase;
    flashcard: Flashcard;
  }): Promise<number> {
    const content = `Notes:

    '''
    ${args.testCase.notes}
    '''

    Flashcard:

    Question: ${args.flashcard.front}
    Answer: ${args.flashcard.back}
    `;

    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo-1106',
      temperature: 0.0,
      n: 1,
      max_tokens: 1,
      messages: [
        {
          role: 'system',
          content: this.prompt,
        },
        {
          role: 'user',
          content: content,
        },
      ],
    });

    const rawContent = response.choices[0].message.content.trim();

    if (rawContent === '0') {
      return 0;
    } else if (rawContent === '1') {
      return 1;
    }

    throw new Error(`Unexpected response: ${rawContent}`);
  }

  async evaluateTestCase(args: {
    testCase: TestCase;
    output: Flashcard[];
  }): Promise<Evaluation> {
    // Score each flashcard asynchronously
    const scores = await Promise.all(
      args.output.map((flashcard) =>
        this.scoreFlashcard({ testCase: args.testCase, flashcard }),
      ),
    );

    if (!scores.length) {
      throw new Error('No scores were returned');
    }

    // Return the average score as the evaluation score
    return { score: scores.reduce((a, b) => a + b, 0) / scores.length };
  }
}
