function ButtonDecorator(props) {
    return window.wagtailDraftail.createElement('span', {
        'data-tooltip': props.entityKey,
        className: 'RichEditor-button',
    }, props.children);
}

window.wagtailDraftail.registerDecorators({
    ButtonDecorator: ButtonDecorator,
});
