import {
  AutoblocksJsxTracer,
  AutoblocksPlaceholder,
} from '@autoblocks/client/ai-jsx';
import {
  ChatCompletion,
  UserMessage,
  SystemMessage,
} from 'ai-jsx/core/completion';
import * as AIJSX from 'ai-jsx';

function GetThingColor(props: { thing: string }) {
  return (
    <ChatCompletion
      temperature={0}
      model="gpt-3.5-turbo"
      autoblocks-tracker-id="get-thing-color"
    >
      <SystemMessage>
        You are a helpful assistant. Always respond with one word in all
        lowercase letters and no punctuation.
      </SystemMessage>
      <UserMessage>
        What color is the{' '}
        <AutoblocksPlaceholder name="thing">
          {props.thing}
        </AutoblocksPlaceholder>
        ?
      </UserMessage>
    </ChatCompletion>
  );
}

function DetermineColorCombination(props: { color: string; thing: string }) {
  return (
    <ChatCompletion
      temperature={0}
      model="gpt-3.5-turbo"
      autoblocks-tracker-id="determine-color-combination"
    >
      <SystemMessage>
        You are an expert in colors. Always respond with one word in all
        lowercase letters and no punctuation.
      </SystemMessage>
      <UserMessage>
        What do you get when you mix{' '}
        <AutoblocksPlaceholder name="color">
          {props.color}
        </AutoblocksPlaceholder>{' '}
        with <GetThingColor thing={props.thing} />?
      </UserMessage>
    </ChatCompletion>
  );
}

async function main() {
  await AIJSX.createRenderContext().render(
    <AutoblocksJsxTracer>
      <DetermineColorCombination color="red" thing="sky" />
    </AutoblocksJsxTracer>,
  );
}

main();
