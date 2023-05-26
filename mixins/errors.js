export default {
  data: () => ({
  }),
  methods: {
    actionFail(response) {
      this.parseError(response);
      this.showErrorDev({ summary: response, detail: response });
    },

    parseError(r) {
      const res = r ? r.response : '';
      const error = res ? (res.data || res) : '';
      if (!(/[a-zA-Z]/.test(error))) {
        return this.showError({ detail: error });
      }
      if (error === 'Incorrect parameters in calculation request') {
        return this.showError({ detail: 'Не удалось обработать запрос. Проверьте правильность заполнения полей.' });
      }
      return this.showError({ detail: 'Не удалось обработать запрос. Проверьте правильность заполнения полей или повторите попытку позднее.' });
    },

    showError({
      detail,
      summary = 'Ошибка:',
      life = 5000,
      closable = true,
      icon = 'pi pi-exclamation-triangle'
    }) {
      this.$toast.add({
        summary,
        detail,
        life,
        closable,
        icon,
        severity: 'error',
      });
    },
    showErrorDev(message) {
      if (process.env.NODE_ENV === 'development') {
        const messageLocal = { ...message, life: null };
        const res = messageLocal.detail;
        messageLocal.detail = res ? (res.response ? (res.response.data || res.response) : '') : '';

        this.showError(messageLocal);
      }
    },

    showSuccess({
      detail,
      summary = 'Запрос успешно отправлен',
      life = 5000,
      closable = true,
      icon = 'pi pi-check-circle'
    }) {
      this.$toast.add({
        summary,
        detail,
        life,
        closable,
        icon,
        severity: 'success',
      });
    },
  },
};
