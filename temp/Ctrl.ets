@controller
class ${CTRL} extends ModelCtrl<${VIEWMODEL}> {

    init() {
		this._viewModel = ViewModelFactory.create(${VIEWMODEL});
	}
}