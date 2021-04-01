import Accordion from './accordion';

describe('Accordion', () => {
    /* eslint-disable no-new */

    beforeEach(() => {
        document.body.innerHTML = `
            <div class="accordion" data-accordion>
                <a class="accordion__title" data-accordion-question aria-expanded="false" tabindex="0">What goes on and on and has an i in the middle?</a>
                <div class="accordion__content" data-accordion-answer aria-hidden="true">
                    An Onion
                </div>
            </div>
        `;
    });

    it('does not show the answer by default', () => {
        new Accordion(document.querySelector(Accordion.selector()));
        expect(
            document
                .querySelector('[data-accordion-answer]')
                .getAttribute('aria-hidden'),
        ).toBe('true');
    });

    it('shows the answer when the question is clicked', () => {
        new Accordion(document.querySelector(Accordion.selector()));

        const question = document.querySelector('[data-accordion-question]');

        question.dispatchEvent(new Event('click'));
        expect(
            document
                .querySelector('[data-accordion-answer]')
                .getAttribute('aria-hidden'),
        ).toBe('false');
    });

    it('hides the answer when the question is clicked if already open', () => {
        new Accordion(document.querySelector(Accordion.selector()));

        const question = document.querySelector('[data-accordion-question]');

        question.dispatchEvent(new Event('click'));
        expect(
            document
                .querySelector('[data-accordion-answer]')
                .getAttribute('aria-hidden'),
        ).toBe('false');

        question.dispatchEvent(new Event('click'));
        expect(
            document
                .querySelector('[data-accordion-answer]')
                .getAttribute('aria-hidden'),
        ).toBe('true');
    });
});
