export default {
  data: () => ({
  }),
  methods: {
    showError({
      detail,
      summary = 'Ошибка',
      life = 3000,
      closable = false,
      src = '/error.svg',
    }) {
      this.$toast.add({
        src,
        summary,
        detail,
        life,
        closable,
        severity: 'error',
      });
    },
    showSuccess({
      detail,
      summary = 'Запрос успешно отправлен',
      life = 3000,
      closable = false,
      src = '/success.svg',
    }) {
      this.$toast.add({
        src,
        summary,
        detail,
        life,
        closable,
        severity: 'success',
      });
    },
  },
};
