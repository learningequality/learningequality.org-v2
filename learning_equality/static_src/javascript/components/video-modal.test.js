import VideoModal from './video-modal';

describe('VideoModal', () => {
    /* eslint-disable no-new */

    beforeEach(() => {
        document.body.innerHTML = `<div data-video-modal>
                <a data-modal-open>Open video</a>
                <div data-modal-window class="video-modal">
                    <a data-modal-close>close</a>
                    <iframe src="foo" />
                </div>
            </div>`;
    });

    it('does not show the iframe by default', () => {
        new VideoModal(document.querySelector(VideoModal.selector()));

        expect(document.querySelector('[data-modal-window]').className).toBe(
            'video-modal',
        );
    });

    it('shows the iframe when the open button is clicked', () => {
        new VideoModal(document.querySelector(VideoModal.selector()));

        const openButton = document.querySelector('[data-modal-open]');
        openButton.dispatchEvent(new Event('click'));
        expect(document.querySelector('[data-modal-window]').className).toBe(
            'video-modal open',
        );
    });

    it('hides the iframe when the close button is clicked', () => {
        new VideoModal(document.querySelector(VideoModal.selector()));

        const openButton = document.querySelector('[data-modal-open]');
        openButton.dispatchEvent(new Event('click'));
        expect(document.querySelector('[data-modal-window]').className).toBe(
            'video-modal open',
        );

        const closeButton = document.querySelector('[data-modal-close]');
        closeButton.dispatchEvent(new Event('click'));
        expect(document.querySelector('[data-modal-window]').className).toBe(
            'video-modal',
        );
    });
});
